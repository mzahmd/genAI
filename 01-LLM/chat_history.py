import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("Type 'exit' to quit.")
user_input = input("User: ")

messages = []

while user_input.strip().lower() != "exit":
    messages.append({"role": "user", "parts": [{"text": user_input}]})
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=messages,
    )
    messages.append({"role": "model", "parts": [{"text": response.text}]})
    print(f"AI: {response.text}")
    user_input = input("User: ")
