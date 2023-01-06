import os, dotenv, openai, sys
from twilio.rest import Client
#use dotenv to load the API key from the .env file

dotenv.load_dotenv()


key = os.environ['OPEN_KEY']
twilio_key = os.environ['TWIL_AUTH']
twilio_sid = os.environ['TWIL_SID']
sender = os.environ['SEND']
receiver = os.environ['REC1']

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