import openai
import os

openai.api_key = os.environ['OPENAI_API_KEY']
# AIのキャラ設定を書き込む

with open("system.txt", 'r') as f:
    configuration = f.read()

Messages = []
Messages.append({"role": "system", "content": configuration})

def ask_chat_gpt():
    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=Messages
    )
    answer = response['choices'][0]['message']['content']
    Messages.append({"role":"assistant", "content":answer})
    return answer

while True:
    user_input = input("私 >")
    if user_input == "":
        break
    Messages.append({"role":"user", "content":user_input})
    answer = ask_chat_gpt()
    print("AI >" + answer)
