# Import packages

import os
import json
# import Email Data Extraction-Subject
import Extract_Data_From_Email as emailHelper

delimiter = '#####'
email_text = ""

# Create prompt to extract Phone Number  from email

prompt = f""" 
You are an intelligent business analysst in a large bank. You have been tasked with extracting Phone numnber from the given email.
The email is as follows: 
{email_text}
{delimiter}
You must extract the Phone number from the email and return them in a list in JSON format {{'PhoneNumber': '<value>'}}. You can find the Phone number in email subject or in email body or in both places.
{delimiter}
Here are some instructions to extract ISINs from the email:
1. Phone number is generally presented at the end  of the email.
2. Phone number is generally prefixed by Phone Number: or Phone: or Ph: or Ph No: or Phone No: or Phone Number: or Phone No.: or Tel: or Telephone: or Telephone No: or Telephone Number: or Telephone No.:
3. Phone number is generally followed by a space and then the phone number.
4. If the phone number with '+' followed by country code, then capture the country code as well.

{delimiter}
Here are few examples to extract ISINs from the email:
{delimiter}
Example 1:
{delimiter}
Email:
from:	Tata Neu <noreply@info.tataneu.com>
reply-to:	noreply@info.tataneu.com
to:	sakpan.sayak@gmail.com
date:	Feb 9, 2025, 7:49 PM
subject:	You've earned 1.24 NeuCoin(s)
mailed-by:	delivery.info.tataneu.com
signed-by:	info.tataneu.com
Shop more and earn more!
Hi Sayak,
You've got 1.24 NeuCoin(s) on your bigbasket order BNN-1635301337-20250209. You can use these NeuCoins on your favourite brands after 17-02-2025.
The promotional NeuCoins, if any, will reflect in your account within 72 hours.
Thanks,
Team Tata Neu
Phone Number: +91 9876543210
{delimiter}
Output:
{{'PhoneNumber': '+91 9876543210'}}
{delimiter}
If you are unable to find the Phone number in the email, return an empty value like this: {{'PhoneNumber': ''}}
"""

messages = []
messages.append({
    "role": "system",
    "content": prompt
})

# Read the email
with open('Data\ISIN Email.txt') as f:
    email_text = f.readlines()

# Convert the email to string
email_text = ''.join(email_text)

# Extract the Phone Number from the email
phone_number = emailHelper.callChatCompletion(messages,email_text)
print(phone_number)
