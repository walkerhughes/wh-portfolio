import io 
import joblib 
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np 

from string import Template
from openai import OpenAI
import json

test_language = "Portuguese"
used_idioms = set()
with open("./llm_prompts/page_2/json_prompt.txt", "r") as infile: 
    json_prompt = Template(infile.read()) 
    json_prompt = json_prompt.substitute(
        language = test_language, 
        used_idioms = used_idioms
    )

client = OpenAI(api_key = "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")

chat = client.chat.completions.create(
    model = "gpt-3.5-turbo",
    messages = [{"role": "user", "content": json_prompt}],
)

llm_response = json.loads(chat.choices[0].message.content)


def format_question(question_json):

    question = "Idiom: {}\n\nIn a sentence: {}\n\nAnswers:\n".format(
        question_json["idiom"],
        question_json["context"][0]
    )

    st.write(question)

    col1, col2, col3 = st.columns(3)
    button1_clicked = col1.button(question_json["multiple_choice"][0])
    button2_clicked = col2.button(question_json["multiple_choice"][1])
    button3_clicked = col3.button(question_json["multiple_choice"][2])

    if button1_clicked:
        st.write("Button 1 was clicked")
    elif button2_clicked:
        st.write("Button 2 was clicked")
    elif button3_clicked:
        st.write("Button 3 was clicked")


format_question(llm_response)