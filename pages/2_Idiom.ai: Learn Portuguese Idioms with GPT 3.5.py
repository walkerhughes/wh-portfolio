from openai import OpenAI
from string import Template
import streamlit as st
from utils.page2_utils import IdiomGame

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

user_lang_option = st.selectbox('Pick a language to get started :point_down:', 
                                    ('Portuguese 🇧🇷', 
                                     'Spanish 🇲🇽', 
                                     'French 🇫🇷', 
                                     'Italian 🇮🇹', 
                                     'German 🇩🇪')
                                    )

user_avatar = "🇺🇸"
test_language = user_lang_option.split(" ")[0]
assistant_avatar = languages[test_language]

with st.chat_message("assistant", avatar = assistant_avatar): 
    st.write(open("./llm_prompts/page_2/initial_assistant_prompt.txt").read())
    

def chat(user_lang_option, OPENAI_API_KEY): 

    client = OpenAI(
        api_key = OPENAI_API_KEY
    ) 

    game = IdiomGame(
        client = client, 
        session_state = st.session_state, 
        language = test_language, 
        user_avatar = user_avatar, 
        assistant_avatar = assistant_avatar
    )

    if "openai_model" not in st.session_state: 
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    with st.chat_message("assistant", avatar = assistant_avatar): 
        st.write(game.display_user_ready_check())

        button1_clicked = st.button(f"Let's get learning {game.language} idioms!")

        if button1_clicked and ("messages" not in st.session_state):
            # append the assistant messages so far and get a question 
            # using the get_json method 
            st.session_state.messages = [{
                "role": "user",
                "content": game.display_user_game_prompt()
            }]
            game.ready_to_play = True

    if game.ready_to_play: 
        game.get_assistant_response()
        for message in st.session_state.messages[1: ]: 
            with st.chat_message(message["role"], avatar = game.avatars[message["role"]]): 
                st.markdown(message["content"])

        if prompt := st.chat_input("Type your response here"): 

            with st.chat_message("user", avatar = user_avatar): 
                st.markdown(prompt)

            st.session_state.messages.append({
                "role": "user",
                "content": prompt
            })

            game.get_assistant_response()



if OPENAI_API_KEY is not None: 
    chat(user_lang_option, OPENAI_API_KEY) 
    
