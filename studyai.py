response = openai.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful study tutor."},
        {"role": "user", "content": question}
    ]
)
answer = response.choices[0].message.content
