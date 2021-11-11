import discord
import os
import requests
import json
from keep_alive import keep_alive

client = discord.Client()

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")
  json_data = json.loads(response.text)
  quote = json_data[0]['q'] + " -" + json_data[0]['a']
  return(quote)

def aws_quote():
  response = requests.get("https://dfsg6ybss8.execute-api.us-east-2.amazonaws.com/default/hello-world-python")
  json_data = json.loads(response.text)
  return json_data

@client.event
async def on_ready():
  print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
  message.content = message.content.lower()
  if message.author == client.user:
    return

  if 'pls henry' in message.content:
    await message.channel.send('<@152153136151134211>')

  if 'pls dino' in message.content:
    quote = aws_quote()
    await message.channel.send(quote)

  if 'pls inspire' in message.content:
    quote = get_quote()
    await message.channel.send(quote)

  if 'pls hello' in message.content:
    await message.channel.send('Hello!')

  if 'pls help' in message.content:
    await message.channel.send("dino, inspire, hello, attention")

  if 'pls attention' in message.content:
    await message.channel.send('@everyone')
keep_alive()
client.run(os.getenv('TOKEN'))