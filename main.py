import os, dotenv, openai, sys
from twilio.rest import Client
#use dotenv to load the API key from the .env file

key = dotenv.get_key(".env", "OPEN_KEY")
twilio_key = dotenv.get_key(".env", "twil_auth")
twilio_sid = dotenv.get_key(".env", "twil_sid")
sender = dotenv.get_key(".env", "number_send")
receiver = dotenv.get_key(".env", "number_rec")

openai.api_key = key
client = Client(twilio_sid, twilio_key)


response = openai.Completion.create(
  model="text-davinci-003",
  prompt="I am someone who will say a pickup line. I will pick a completely random pickup line today. Today my pickup line is: ",
  temperature=0.8,
  max_tokens=60,
  top_p=1.0,
  frequency_penalty=0.0,
  presence_penalty=0.0
)

store = response.choices[0].text
print(store)
message = client.messages.create(
    body=store,
    from_=sender,
    to=receiver)
print(message.sid)