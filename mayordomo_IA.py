#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
from groq import Groq

client = Groq(
    api_key="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"
)
pregunta = input("Escribe tu pregunta:")
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": pregunta,
        }
    ],
    model="llama3-8b-8192",
)

print(chat_completion.choices[0].message.content)