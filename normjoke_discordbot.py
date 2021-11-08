from normjokes_scrapper import get_joke
from random import randint
import discord
from discord.ext import commands

jokelist = []

for i in range(407):
    jokelist.append(get_joke(i))
    print('Loaded joke index ' + str(i) + ' of 406')
else:
    print('Jokes loaded')

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

bot.run('token')