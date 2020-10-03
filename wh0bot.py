import discord
from discord.ext import commands
from pathlib import Path 
import json


#Basic setup
cwd = Path(__file__).parents[0]
cwd = str(cwd)

secret_file = json.load(open(cwd+'/Token.json'))
client = commands.Bot(command_prefix = '-')
token = secret_file['token']

@client.event 
async def on_ready():
    print('Wh0 cares Iv arrived?.')

@client.command()
async def ping(ctx):
     await ctx.send(f'Hello Yes, what do you want? Its only been {round(client.latency * 1000)}ms')

@client.command()
async def say(ctx,arg):
    await ctx.send(f"{arg}")

#Hardcoded Moderation
@client.command()
async def clear(ctx,amount=1):
    await ctx.channel.purge(limit=amount+1)
    if (amount==1):
        await ctx.send(f"successfully cleared {amount} message") 
    else:
        await ctx.send(f"successfully cleared {amount} messages") 



client.run(token) 