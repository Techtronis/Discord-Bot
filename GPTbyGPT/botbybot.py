import discord
import asyncio
from chatgpt import ChatGPT

TOKEN = ''

client = discord.Client()

@client.event
async def on_ready():
    print(f'Logged in as {client.user.name}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.content.startswith('$chatgpt'):
        # create a chatgpt instance
        chatbot = ChatGPT()
        # get the user's input
        user_input = message.content.split(' ', 1)[1]
        # get the chatbot's response
        response = chatbot.get_response(user_input)
        # send the response to the user
        await message.channel.send(response)

client.run(TOKEN)
