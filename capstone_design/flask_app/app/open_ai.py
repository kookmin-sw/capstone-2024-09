from flask import Flask, request, jsonify
from dotenv import load_dotenv
import os
from openai import OpenAI

load_dotenv()
client = OpenAI()
app = Flask(__name__)
client.key = os.getenv("OPENAI_API_KEY")

def request_openai(message):
    MODEL = "gpt-3.5-turbo"
    system_message = {
        "role": "system",
        "content": "You are a caring and understanding career counselor for teenagers. Your role is to provide guidance, advice and encouragement to help them explore potential career paths that align with their interests, skills and values. Be supportive, non-judgmental and frame your responses in a positive, motivating way."
    }
    user_message = {"role": "user", "content": message}
    messages = [system_message, user_message]

    try:
        with app.app_context():
            response = client.chat.completions.create(
                model=MODEL,
                messages=messages,
                temperature=0,
            )

        result = response.choices[0].message.content
        return {"result": result}
    except Exception as e:
        print(e)
        return {"error": "An error occurred while fetching the response"}

