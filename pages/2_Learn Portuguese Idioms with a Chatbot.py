from openai import OpenAI
from string import Template
import streamlit as st
from utils.page2_utils import get_assistant_response

st.set_page_config(
    page_title = "Idiom.ai", 
    page_icon=":speech_balloon:"
)

st.title(":speech_balloon: Idiom.ai")

with st.sidebar:
    OPENAI_API_KEY = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password", value = None)
    "[Need an OpenAI API key?](https://platform.openai.com/account/api-keys)"

welcome_message = """
    Welcome to Idiom.ai! Understanding figurative language is hard enough in your mother tongue, and even harder in a foreign language. \
    This chatbot powered by OpenAI's GPT 3.5 Turbo leverages generative AI in a gamified format to make learning a foreign language's 
    idioms fun and effective.
"""

st.write(welcome_message)

languages = {
    'Portuguese': "🇧🇷", 
    'Spanish': "🇲🇽",
    'French': "🇫🇷",
    'Italian': "🇮🇹",
    'German': "🇩🇪"
}

user_lang_option = st.selectbox('Pick a language to get started', 
                                    ('Portuguese 🇧🇷', 
                                     'Spanish 🇲🇽', 
                                     'French 🇫🇷', 
                                     'Italian 🇮🇹', 
                                     'German 🇩🇪')
                                    )

def chat(user_lang_option, OPENAI_API_KEY) -> None: 

    user_avatar = "🇺🇸"
    test_language = user_lang_option.split(" ")[0]
    assistant_avatar = languages[test_language]

    avatars = {
        "user": user_avatar, 
        "assistant": assistant_avatar
    }

    if "openai_model" not in st.session_state: 
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    with open("./llm_prompts/page_2/initial_game_prompt.txt", "r") as infile: 
        game_prompt_template = Template(infile.read())
        game_prompt = game_prompt_template.substitute(language = test_language) 

    with open("./llm_prompts/page_2/initial_assistant_prompt.txt", "r") as infile: 
        assistant_prompt_template = Template(infile.read())
        assistant_prompt = assistant_prompt_template.substitute(language = test_language) 

    client = OpenAI(api_key = OPENAI_API_KEY) 

    if "messages" not in st.session_state: 
        st.session_state.messages = [{
            "role": "user",
            "content": game_prompt
        }] 
        # get_assistant_response(client, st.session_state, assistant_avatar)
        st.session_state.messages = [{
            "role": "assistant",
            "content": assistant_prompt
        }]
        with st.chat_message("assistant", avatar = user_avatar): 
            st.markdown(assistant_prompt)

    for message in st.session_state.messages[1: ]: 
        with st.chat_message(message["role"], avatar = avatars[message["role"]]): 
            st.markdown(message["content"])

    if prompt := st.chat_input("Type your response here"): 

        with st.chat_message("user", avatar = user_avatar): 
            st.markdown(prompt)

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        get_assistant_response(client, st.session_state, assistant_avatar)
 

if OPENAI_API_KEY is not None: 
    chat(user_lang_option, OPENAI_API_KEY) 