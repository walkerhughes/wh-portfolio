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



class IdiomGame:
    def __init__(self, client, session_state, language, assistant_avatar):
        self.__dict__.update(locals())
        self.message_template = {
            "role": None,
            "content": None
        }

        self.score = 0

    def display_welcome_message(self):
        return """
            Welcome to Idiom.ai! 👋 Get ready for some awesome language practice.\n \
            
            **Here's how the game works**:\n \
            1. Pick a language from the dropdown menu, and I'll give you a common idiom or figure of speech in that language along with an example of it being used in a sentence.\n \
            2. You'll get to choose its correct meaning from a list of 3 options. If you get it right first try, that's 1 point!\n \
            3. No worries if you don't get it right on the first try. You can still get a half point for getting it right on the second guess.\n \
        """
    
    def display_user_ready_check(self):
        return f"You've chosen {self.language}. Ready to get started?"

    def format_message(self, session_state_message): 
        return {"role": session_state_message["role"], "content": session_state_message["content"]}
    
    def get_current_chat(self): 
        current_chat = self.client.chat.completions.create(
            model = self.session_state["openai_model"],
            messages = [format_message(message) for message in self.session_state.messages],
            stream = True
        )
        return current_chat

    def get_assistant_response(self): 

        with st.chat_message("assistant", avatar = self.assistant_avatar): 

            assistant_message = st.empty() 
            assistant_response = "" 

            current_chat = self.get_current_chat(self.client, self.session_state)

            for response in current_chat: 
                chunk = response.choices[0].delta.content
                if chunk is not None: 
                    assistant_response += response.choices[0].delta.content 
                assistant_message.markdown(assistant_response + " ")
            assistant_message.markdown(assistant_response)

        self.session_state.messages.append({
            "role": "assistant",
            "content": assistant_response
        })

    def update_score(self, correct):
        if correct:
            self.score += 1
        else:
            self.score += 0.5  
    
    def play(self):
        pass
