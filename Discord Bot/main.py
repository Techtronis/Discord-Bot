import discord
import random
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
bot = commands.Bot(command_prefix='!', intents=intents)

@bot.command()
async def helpme(ctx):
    await ctx.send("""!spam : Will spam number
!rand10 : Will choose a random number between 1-10
!rand100 : will choose a random number between 1-100
!rps : Choose Rock, Paper or Scissors to play with the bot""")

@bot.command()
async def spam(ctx):
    y = 0
    while(y < 10):
        y+1
        await ctx.send(y)
  
@bot.command()
async def rand10(ctx):
    i = random.randint(1,10)
    await ctx.send(i)

@bot.command()
async def rand100(ctx):
    i = random.randint(1,100)
    await ctx.send(i)

@bot.command()
async def rps(ctx, arg):
    playerChoice = str(arg)

    if playerChoice == "rock":
        playerChoiceInt = 0
    elif playerChoice == "paper":
        playerChoiceInt = 1
    elif playerChoice == "scissors":
        playerChoiceInt = 2
    elif playerChoice == "Paper":
        playerChoiceInt = 1
    elif playerChoice == "Scissors":
        playerChoiceInt = 2
    elif playerChoice == "Rock":
        playerChoiceInt = 0

    botChoiceInt = random.randint(0,2)

    #Rock = 0 Paper = 1 Scissors = 2  

    # 0 beats 2
    if playerChoiceInt == 2:
        if botChoiceInt == 0:
            await ctx.send("I chose Rock, You lose!")
            print("I chose Rock, You lose!")

    elif playerChoiceInt == 0:
        if botChoiceInt == 2:
            await ctx.send("I chose Scissors, You win!")
            print("I chose Scissors, You win!")

    # 1 beats 0
    if playerChoiceInt == 1:
        if botChoiceInt == 0:
            await ctx.send("I chose Rock, You lose!")
            print("I chose Rock, You lose!")

    elif playerChoiceInt == 0:
        if botChoiceInt == 1:
            await ctx.send("I chose Paper, You win!")
            print("I chose Paper, You win!")
    # 2 beats 1
    if playerChoiceInt == 2:
        if botChoiceInt == 1:
            await ctx.send("I chose Paper, You lose!")
            print("I chose Paper, You lose!")

    elif playerChoiceInt == 1:
        if botChoiceInt == 2:
            await ctx.send("I chose Scissors, You win!")
            print("I chose Scissors, You win!")

    elif playerChoiceInt == botChoiceInt:
        await ctx.send("It's a draw!")
        print("It's a draw!")
    
    #await ctx.send(playerChoiceInt)
    #await ctx.send(botChoiceInt)

print("----------------------")
print("| The bot is running |")
print("----------------------")


bot.run('Put token here')
