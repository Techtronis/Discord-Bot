import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='', intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')

@bot.command()
async def rand10(ctx):
    i = random.randint(1,10)
    await ctx.send(i)

@bot.command()
async def rand100(ctx):
    f = random.randint(1,100)
    await ctx.send(f)

@bot.command()
async def RevealTheTruth(ctx):
    await ctx.send("@Philemax is gay")

@bot.command()
async def spam(ctx):
    for x in range(100000000):
        await ctx.send(x)
    
        

print("----------------------")
print("| The bot is running |")
print("----------------------")


bot.run('token')
