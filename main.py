import os
from mistralai import Mistral

api_key = ""
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model = model,
    messages = [
        {
            "role": "user",
            "content": "Coucou , est-ce que tu peux me dire combien il y a t-il de planètes dans le systeme solaire ?",
        },
    ]
)

print(chat_response.choices[0].message.content)