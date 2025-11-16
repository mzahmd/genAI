import os
from dotenv import load_dotenv
from google import genai

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

print("Type 'exit' to quit.")
user_input = input("User: ")

while user_input.strip().lower() != "exit":
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=user_input,
    )
    print(f"AI: {response.text}")
    user_input = input("User: ")
