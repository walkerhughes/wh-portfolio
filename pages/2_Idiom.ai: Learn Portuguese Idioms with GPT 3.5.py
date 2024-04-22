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
        game_play = st.button(f"Let's get learning {game.language} idioms!")
        if game_play and ("messages" not in st.session_state):
            question = game.get_question_json()
            st.session_state.messages = [{
                "role": "assistant",
                "content": game.format_question(question)
            }]
            game.ready_to_play = True

    if game.ready_to_play: 
        for message in st.session_state.messages: 
            with st.chat_message(message["role"], avatar = game.avatars[message["role"]]): 
                st.markdown(message["content"])
                user_response = False
            
                col1, col2, col3 = st.columns(3)
                button1_clicked = col1.button(question["multiple_choice"][0], key = 7)
                button2_clicked = col2.button(question["multiple_choice"][1], key = 1)
                button3_clicked = col3.button(question["multiple_choice"][2], key = 2)
                if button1_clicked and (question["index"] == 0):
                    user_response = True
                    st.write("Button 1 was clicked")
                elif button2_clicked and (question["index"] == 1):
                    user_response = True
                    st.write("Button 2 was clicked")
                elif button3_clicked and (question["index"] == 2):
                    user_response = True
                    st.write("Button 3 was clicked")


        if prompt := st.chat_input(""): 
            """
            with st.chat_message("user", avatar = user_avatar): 
                st.markdown(prompt)
            """
            st.session_state.messages.append({
                "role": "user",
                "content": prompt
            })

if OPENAI_API_KEY is not None: 
    chat(user_lang_option, OPENAI_API_KEY) 
    
