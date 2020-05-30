import discord
from discord.ext import commands

client= commands.Bot(command_prefix = '-')

@client.event 
async def on_ready():
    print('Wh0 cares Iv arrived?.')

@client.command()
async def ping(ctx):
     await ctx.send(f'Hello Yes, what do you want? Its only been {round(client.latency * 1000)}ms')

client.run('Token')

