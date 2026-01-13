import openai
import os
import streamlit as st

# Load your OpenAI API key safely from Streamlit secrets
openai.api_key = os.getenv("OPENAI_API_KEY")

st.title("StudyAI - Your Study Assistant")

# Get user input
question = st.text_input("Enter a topic or question:")

# Function to call OpenAI
def ask_ai(question):
    try:
        response = openai.chat.completions.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful study tutor."},
                {"role": "user", "content": question}
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"⚠️ Error: {e}"

# Call API only when user clicks button
if st.button("Ask AI"):
    if question:
        answer = ask_ai(question)
        st.write("**AI Answer:**", answer)
