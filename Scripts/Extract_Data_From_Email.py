# import openai

import os
import json
import openai


# Load the JSOn file with the API key
with open('OpenAI API Key.json') as f:
    data = json.load(f)

# Set the API key
openai.api_key = data['Open AI API Key']

# Set the API key in env variable
os.environ['OPENAI_API_KEY'] = openai.api_key



# get sample email

def get_sample_email():
    
    # Load a sample email
    with open('Data\Sample.txt') as f:
        sample_email = f.read()

    return sample_email

def callChatCompletion(messages,email):
    messages.append({"role": "user", "content": email})
    response = openai.chat.completions.create(
                                        model="gpt-4o",
                                        messages = messages,
                                        temperature=0
                                        



                                        
    )
    return response.choices[0].message.content



 
