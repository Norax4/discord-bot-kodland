import discord
import random

from discord.ext import commands
import requests

import os

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='$', intents=intents)

def get_duck_image_url():    
    url = 'https://random-d.uk/api/random'
    res = requests.get(url)
    data = res.json()
    return data['url']

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')

@bot.command(description= "hi")
async def hello(ctx):
    await ctx.send(f'Hola, soy un bot {bot.user}!')

@bot.command(description= "heh")
async def heh(ctx, count_heh = 5):
    await ctx.send("he" * count_heh)

@bot.command(description= "calculator with 13 buttons")
async def add(ctx, left: int, right: int):
    """Adds two numbers together."""
    await ctx.send(left + right)

@bot.command(description = "memes")
async def meme(ctx):
    img_meme = os.listdir('img')
    img_mostrar = random.choice(img_meme)
    with open(f'img/{img_mostrar}', 'rb') as f:
        picture = discord.File(f)
    await ctx.send(file=picture)

@bot.command(description= 'duck pics')
async def duck(ctx):
    '''Una vez que llamamos al comando duck, 
    el programa llama a la función get_duck_image_url'''
    image_url = get_duck_image_url()
    await ctx.send(image_url)

@bot.command(description= "For when you want to roll a dice!")
async def roll(ctx, dice: str):
    """Rolls a dice in NdN format."""
    try:
        rolls, limit = map(int, dice.split('d'))
    except Exception:
        await ctx.send('Format has to be in NdN!')
        return

    result = ', '.join(str(random.randint(1, limit)) for r in range(rolls))
    await ctx.send(result)

@bot.command(description='For when you wanna settle the score some other way')
async def choose(ctx, *choices: str):
    """Chooses between multiple choices."""
    await ctx.send(random.choice(choices))

bot.run("MTIxOTAxNjg3MDAyNDMxNDk5Mg.GtmC3p.AzcOiygGrrZ6DHaIzIqEn69fk5bMTqc20JSfXA")