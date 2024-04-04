from openai import OpenAI
from string import Template
import streamlit as st

message_template = {"role": None, "content": None}

def format_message(session_state_message): 
    return {"role": session_state_message["role"], "content": session_state_message["content"]}

def get_current_chat(client, session_state): 
    current_chat = client.chat.completions.create(
        model = session_state["openai_model"],
        messages = [format_message(message) for message in session_state.messages],
        stream = True
    )
    return current_chat

def get_assistant_response(client, session_state, assistant_avatar): 

    with st.chat_message("assistant", avatar = assistant_avatar): 

        assistant_message = st.empty() 
        assistant_response = "" 

        current_chat = get_current_chat(client, session_state)

        for response in current_chat: 
            chunk = response.choices[0].delta.content
            if chunk is not None: 
                assistant_response += response.choices[0].delta.content 
            assistant_message.markdown(assistant_response + " ")
        assistant_message.markdown(assistant_response)

    session_state.messages.append({
        "role": "assistant",
        "content": assistant_response
    })