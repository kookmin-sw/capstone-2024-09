from dotenv import load_dotenv
import os
from openai import OpenAI
from fastapi import FastAPI

load_dotenv()
client = OpenAI()
app = FastAPI()
client.key = os.getenv("OPENAI_API_KEY")

def get_chat_response(message):
    MODEL = "gpt-3.5-turbo"
    system_message = {
        "role": "system",
        "content": "You are a caring and understanding career counselor for teenagers. Your role is to provide guidance, advice and encouragement to help them explore potential career paths that align with their interests, skills and values. Be supportive, non-judgmental and frame your responses in a positive, motivating way."
    }
    user_message = {"role": "user", "content": message}
    messages = [system_message, user_message]
    try:
        response = client.chat.completions.create(
            model=MODEL,
            messages = messages,
            temperature=0,
        )
        return response.choices[0].message.content
    except Exception as e:
        print(e)
        return {"error": "An error occurred while fetching the response"}