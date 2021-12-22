import pandas

# bot.py
import os

import discord

TOKEN = 'OTE4MTY2NDU2NzQ5OTIwMzQ2.YbDTJQ.Byq9QwEjiZ7NsfH6ZWEKWmNUC1k'
GUILD = 'PGE2 ADAV'

client = discord.Client()

@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})'
    )
            

client.run(TOKEN)

