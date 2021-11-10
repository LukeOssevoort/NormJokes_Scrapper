from normjokes_scrapper import get_jokepickle
from random import randint
import discord
from discord.ext import commands
import pickle

tokenFileName = 'token.pkl'
jokeFileName = 'jokelist.pkl'

try:
    tokenFile = open(tokenFileName,'r')
    token = tokenFile.readline()
    print('Loaded discord token')
    tokenFile.close()
except:
    tokenFile = open(tokenFileName, 'w+')
    token = input('Enter discord bot token: ')
    tokenFile.write(token)
    print('Saved discord token')
    tokenFile.close()

jokelist = get_jokepickle(jokeFileName)

description = '''An example bot to showcase the discord.ext.commands extension
module.
There are a number of utility commands being showcased here.'''

intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix='$', description=description, intents=intents)

@bot.event
async def on_ready():
    print('Logged in as')
    print(bot.user.name)
    print(bot.user.id)
    print('------')

@bot.command()
async def normjoke(ctx, *args: int):
    if len(args) > 0:
        joke = jokelist[args[0]]
    else:
        joke = jokelist[randint(0,406)]

    await ctx.send(joke.text.replace('\n','\n\n') + '\n\n' + joke.ep + '\n' + joke.guest)

bot.run(token)