import discord
from discord.ext import commands, tasks
from datetime import datetime, timedelta
import asyncio
from dotenv import load_dotenv
load_dotenv()

TOKEN = os.getenv('TOKEN')
intents = discord.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

def getTextFromFile(n):
    text = '```'
    with open(f"/outputs/sl_output_{n}.txt", 'r') as file:
        text += file.read()
    text += '```'
    return(text)

@bot.command(name = "sl")
async def sl(ctx):
    msg = await ctx.send(getTextFromFile(1))
    for i in range(2,204):
        await msg.edit(content=getTextFromFile(i))
        await asyncio.sleep(0.5)

    await msg.delete()

@bot.event
async def on_ready():
    print('Logged in as {0.user}'.format(bot))
    

bot.run(TOKEN)
