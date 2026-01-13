import openai
import os
import streamlit as st

# Correct way to load API key from Streamlit secret
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("StudyAI - Your Study Assistant")

question = st.text_input("Enter a topic or question:")

if st.button("Ask AI"):
    if question:
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a helpful study tutor."},
                    {"role": "user", "content": question}
                ]
            )
            answer = response.choices[0].message.content
            st.write("**AI Answer:**", answer)
        except Exception as e:
            st.write("⚠️ Error:", e)