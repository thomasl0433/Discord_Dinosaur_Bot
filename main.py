import discord
import os
import requests
import json

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
  if message.author == client.user:
    return

  if 'pls dino' in message.content:
    quote = aws_quote()
    await message.channel.send(quote)

  if message.content.startswith('$inspire'):
    quote = get_quote()
    await message.channel.send(quote)

  if message.content.startswith('$hello'):
    await message.channel.send('Hello!')

  if message.content.startswith("$k'"):
    await message.channel.send('ebekashiest')

  if message.content.startswith("$fuck you"):
    await message.channel.send('gladly')

client.run(os.getenv('TOKEN'))