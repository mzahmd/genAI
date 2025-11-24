import os
from dotenv import load_dotenv
from google import genai
import csv

# to read and index CSV files
from lunr import lunr

load_dotenv()

client = genai.Client(api_key=os.getenv("GOOGLE_API_KEY"))

def generate_response(prompt: str) -> str:
  response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt,
  )
  return response.text.strip()


with open("hybrid.csv", 'r', encoding='utf-8') as file:
  csv_reader = csv.reader(file, delimiter=',')
  csv_data = list(csv_reader)
  # print(csv_reader)
  # print(csv_data)

documents = [{"id": i, "body": " ".join(row)} for i, row in enumerate(csv_data)]
print(documents[:2])

# index = lunr(ref="id", fields=("body",), documents=documents)
index = lunr(ref="id", fields=["body"], documents=documents)
print(index)


if __name__ == "__main__":
  print("Type 'exit' to quit.\n\n")

  messages = []
  user_input = input("User: ")

  print(index.search(user_input))

  # while user_input.strip().lower() != "exit":
    
  #   # history tracking
  #   messages.append({"role": "user", "parts": [{"text": user_input}]})

  #   ai_response = generate_response(messages)
    
  #   # history tracking
  #   messages.append({"role": "model", "parts": [{"text": ai_response}]})
    
  #   print(f"AI: {ai_response}")
    
  #   user_input = input("User: ")
