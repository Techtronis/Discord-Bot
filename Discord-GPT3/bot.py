import discord
import openai
from discord.ext import commands

openai.api_key = ""

intents = discord.Intents.default()
intents.message_content = True

token = ""

gpt = discord.Client(intents = intents)
bot = commands.Bot(command_prefix='!', intents=intents)

@gpt.event
async def on_ready():
    print("Bot is connected.")

@gpt.event
async def on_message(message):

     username = str(message.author).split('#')[0]
     user_message = str(message.content)
     channel = str(message.channel.name)

     print(username + ": " + user_message)

     if message.author == gpt.user:
          return
     
     if channel != "chat-gpt":
          return
     
  
     response = openai.Completion.create(
          model = "text-davinci-003",
          prompt = user_message,
          max_tokens = 1000,
          temperature =0.7
          )

     output = response["choices"][0]["text"]
     await message.channel.send(output)
   
gpt.run(token)
