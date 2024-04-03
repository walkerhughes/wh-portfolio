from openai import OpenAI
from string import Template
import streamlit as st

st.set_page_config(
    page_title = "Idiom.ai", 
    page_icon=":speech_balloon:"
)

st.title(":speech_balloon: Idiom.ai")

with st.sidebar:
    openai_api_key = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password")
    "[Need an OpenAI API key?](https://platform.openai.com/account/api-keys)"

welcome_message = """
    Welcome to Idiom.ai! Understanding figurative language is hard enough in your mother tongue, and even harder in a foreign language. \
    This chatbot powered by OpenAI's GPT 3.5 Turbo leverages generative AI in a gamified format to make learning a foreign language's 
    idioms fun and effective.
"""

st.write(welcome_message)

languages = {
    'English': "🇺🇸", 
    'Portuguese': "🇧🇷", 
    'Spanish': "🇲🇽",
    'French': "🇫🇷",
    'Italian': "🇮🇹",
    'German': "🇩🇪"
}

with open("./llm_prompts/page_2/initial_game_prompt.txt", "r") as infile: 
    game_prompt_template = Template(infile.read())

def chat() -> None: 

    user_lang_option = st.selectbox('Pick a language to get started', ('English', 'Portuguese', 'Spanish', 'French', 'Italian', 'German'))

    if "messages" not in st.session_state:
        st.session_state["messages"] = [{"role": "assistant", "content": "Ready to begin?"}]

    for msg in st.session_state.messages:
        st.chat_message(msg["role"]).write(msg["content"])

    if prompt := st.chat_input():
        if not openai_api_key:
            st.info("Please add your OpenAI API key to continue.")
            st.stop()

        client = OpenAI(api_key=openai_api_key)
        st.session_state.messages.append({"role": "user", "content": game_prompt_template.substitute(language = user_lang_option)})
        st.chat_message("user").write(prompt)
        response = client.chat.completions.create(model="gpt-3.5-turbo", messages=st.session_state.messages)
        msg = response.choices[0].message.content
        st.session_state.messages.append({"role": "assistant", "content": msg})
        st.chat_message("assistant").write(msg)

chat() 