from openai import OpenAI
from string import Template
import streamlit as st
import json

message_template = {"role": None, "content": None}

class IdiomGame:
    def __init__(self, client, session_state, language, user_avatar, assistant_avatar):
        
        self.__dict__.update(locals())
        self.score = 0
        self.ready_to_play = False
        self.used_idioms = set()

        self.message_template = {
            "role": None,
            "content": None
        }

        self.avatars = {
            "user": user_avatar, 
            "assistant": assistant_avatar,
            "system": assistant_avatar
        }

        with open("./llm_prompts/page_2/json_prompt.txt", "r") as infile: 
            json_prompt = Template(infile.read()) 
            self.json_prompt = json_prompt.substitute(
                language = self.language, 
                used_idioms = self.used_idioms
            )

    def display_welcome_message(self):
        return """
            Welcome to Idiom.ai! 👋 Get ready for some awesome language practice.\n \
            
            **Here's how the game works**:\n \
            1. Pick a language from the dropdown menu, and I'll give you a common idiom or figure of speech in that language along with an example of it being used in a sentence.\n \
            2. You'll get to choose its correct meaning from a list of 3 options. If you get it right first try, that's 1 point!\n \
            3. No worries if you don't get it right on the first try. You can still get a half point for getting it right on the second guess.\n \
        """
    
    def display_user_ready_check(self):
        return f"You picked **{self.language}**. Feel free to pick a different language from the dropdown menu, otherwise click the button below to let me know you're ready for your first challenge."

    def format_message(self, session_state_message): 
        return {"role": session_state_message["role"], "content": session_state_message["content"]}
    
    def get_current_chat(self): 
        current_chat = self.client.chat.completions.create(
            model = self.session_state["openai_model"],
            messages = [self.format_message(message) for message in self.session_state.messages],
            stream = True
        )
        return current_chat
    
    def get_question_json(self): 
        chat = self.client.chat.completions.create(
            model = self.session_state["openai_model"],
            messages = [{
                "role": "user", 
                "content": self.json_prompt
            }],
        )
        llm_response = json.loads(chat.choices[0].message.content)
        self.used_idioms.add(llm_response["idiom"])
        return llm_response

    def update_score(self, correct):
        if correct:
            self.score += 1
        else:
            self.score += 0.5  