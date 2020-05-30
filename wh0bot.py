import discord
from discord.ext import commands
from pathlib import Path 
import json

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



client.run(token) 