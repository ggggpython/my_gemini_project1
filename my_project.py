# https://aistudio.google.com/apikey
import google.generativeai as genai
import dotenv
import os

dotenv.load_dotenv()
API_KEY = os.getenv('API_KEY')

genai.configure(api_key=API_KEY)


model = genai.GenerativeModel('gemini-2.0-flash-exp')


print("Type 'exit' to quit.")
while True:
    user_input = input("Me: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    response = model.generate_content(user_input)
    print("Gemini:", response.text)