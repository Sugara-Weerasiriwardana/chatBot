import time
import openai
import os

#delete the key before commit
openai.api_key = ""

# Function to send a message to ChatGPT and get a response
def chat_with_gpt(message):
    time.sleep(1)
    response = openai.Completion.create(
        engine="omni-moderation-latest",  
        prompt=message,
        max_tokens=50  
    )
    return response.choices[0].text


conversation = []

while True:
    user_input = input("You: ")
    conversation.append(f"You: {user_input}")

    
    if user_input.lower() == 'exit':
        break

    
    response = chat_with_gpt("\n".join(conversation))
    print(f"ChatGPT: {response}")
    conversation.append(f"ChatGPT: {response}")