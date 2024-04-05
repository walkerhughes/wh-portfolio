from openai import OpenAI
from string import Template
import streamlit as st
from utils.page2_utils import get_assistant_response, IdiomGame

st.set_page_config(
    page_title = "Idiom.ai", 
    page_icon=":speech_balloon:"
)

st.title(":speech_balloon: Idiom.ai")

with st.sidebar:
    OPENAI_API_KEY = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password", value = None)
    "[Need an OpenAI API key?](https://platform.openai.com/account/api-keys)"

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

client = OpenAI(api_key = OPENAI_API_KEY) 

game = IdiomGame(
    client = client, 
    session_state = st.session_state, 
    language = test_language, 
    assistant_avatar = assistant_avatar
)

