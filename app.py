import streamlit as st
import openai
from dotenv import load_dotenv
import os

load_dotenv()


# Set your OpenAI API key
openai.api_key = os.getenv('OPENAI_API_KEY')

def transform_to_shakespeare(text):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": "You are a Shakespearean playwright."},
            {"role": "user", "content": f"Translate the following text into the style of Shakespeare: {text}"}
        ]
    )
    return response['choices'][0]['message']['content']

st.title("Shakespearean Translator")

user_input = st.text_area("Enter text to transform:", height=150)

if st.button("Translate"):
    if user_input:
        with st.spinner('Doing Some Magic...'):
            transformed_text = transform_to_shakespeare(user_input)
        st.write("### Transformed Text:")
        st.write(transformed_text)
    else:
        st.error("Please enter some text to transform.")
