import openai
import os

def get_openai_key():
    openai.key = os.getenv("OPENAI_API_KEY")
    return  openai

if __name__ == '__main__':
    openai = get_openai_key()
    print(openai.key)