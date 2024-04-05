from openai import OpenAI
from string import Template
import streamlit as st
from utils.page5_utils import YoutubeVideoRAG

st.set_page_config(
    page_title = "YouTube Video Q&A", 
    page_icon=":tv:"
)

avatars = {
    "user": "❓", 
    "assistant": "📺"
}

st.title(":tv: RAG App for YouTube Video Q&A")

with st.sidebar:
    VIDEO_URL = st.text_input("YouTube Video URL", key="video_url", value = None)

with st.sidebar:
    OPENAI_API_KEY = st.text_input("OpenAI API Key", key="chatbot_api_key", type="password", value = None)
    "[Need an OpenAI API key?](https://platform.openai.com/account/api-keys)"

welcome_message = """
    This is a simple RAG application to query YouTube video transcripts that uses LangChain to \
    perform similarity searches and GPT 3.5 to answer our questions.
"""

st.write(welcome_message)

assistant_prompt = """
    Hey there :wave: Enter your OpenAI API Key and a YouTube Video URL in the left-hand column to get started!
"""

if "messages" not in st.session_state: 
    st.session_state.messages = [{
        "role": "assistant",
        "content": assistant_prompt
    }]

with st.chat_message("assistant", avatar = avatars["assistant"]): 
    st.markdown(assistant_prompt)

def chat(OPENAI_API_KEY, VIDEO_URL) -> None: 

    if "openai_model" not in st.session_state: 
        st.session_state["openai_model"] = "gpt-3.5-turbo"

    query_bot = YoutubeVideoRAG(
        api_key = OPENAI_API_KEY, 
        video_urls = [VIDEO_URL]
    )

    st.session_state.messages = [{
        "role": "assistant",
        "content": "This video has been analyzed! Feel free to start asking questions below :point_down"
    }] 

    for message in st.session_state.messages: 
        with st.chat_message(message["role"], avatar = avatars[message["role"]]): 
            st.markdown(message["content"])

    if prompt := st.chat_input("Type your response here"): 

        with st.chat_message("user", avatar = avatars["user"]): 
            st.markdown(prompt)

        st.session_state.messages.append({
            "role": "user",
            "content": prompt
        })

        assistant_response = query_bot.answer_query(query = prompt)

        with st.chat_message("assistant", avatar = avatars["assistant"]): 
            st.markdown(assistant_response)

        st.session_state.messages.append({
            "role": "assistant",
            "content": assistant_response
        })



if OPENAI_API_KEY is not None and VIDEO_URL is not None: 
    chat(OPENAI_API_KEY, VIDEO_URL) 