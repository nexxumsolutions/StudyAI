import openai

# Paste your API key inside the quotes
openai.api_key = import openai
import os
import streamlit as st

# Get API key from environment variable (safe


def ask_ai(question):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a kind and helpful study tutor."},
            {"role": "user", "content": question}
        ]
    )
    return response.choices[0].message.content

def main():
    print("Welcome to StudyAI!")
    while True:
        topic = input("Enter a topic or question (or type 'exit'): ")
        if topic.lower() == "exit":
            break
        answer = ask_ai(topic)
        print("\nAI Answer:\n", answer)

if __name__ == "__main__":
    main()