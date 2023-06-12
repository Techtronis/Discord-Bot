import discord
import openai

openai.api_key = "Put openAI key here"

intents = discord.Intents.default()
intents.message_content = True

token = "Put discord key here"

bot = discord.Client(intents = intents)

@bot.event
async def on_ready():
    print("Bot is connected.")

@bot.event
async def on_message(message):

     username = str(message.author).split('#')[0]
     user_message = str(message.content)
     channel = str(message.channel.name)

     print(username + ": " + user_message)

     if message.author == bot.user:
          return
     
  
     response = openai.Completion.create(
          model = "text-davinci-003",
          prompt = user_message,
          max_tokens = 3000,
          temperature =0.7
          )

     output = response["choices"][0]["text"]
     await message.channel.send(output)
   
bot.run(token)
