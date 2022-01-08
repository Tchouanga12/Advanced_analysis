import discord
import sys
import os
sys.path.append(os.getcwd())
from FinalProject.Data_Handling_tools.visualize import football

##Personal information of the bit
TOKEN = 'OTE4MTY2NDU2NzQ5OTIwMzQ2.YbDTJQ.XSE8FCuzUPBepLE3yc2PednQs70'
##Discord channel also know as guild
GUILD = 'PGE2 ADAV'

client = discord.Client()

##To know about the bot id, discord channel and bot name
@client.event
async def on_ready():
    for guild in client.guilds:
        if guild.name == GUILD:
            break

    print(
        f'{client.user} is connected to the following guild:\n'
        f'{guild.name}(id: {guild.id})')

##Provide response to users request
@client.event
async def on_message(message):

    if message.content.startswith('hello'):
        await message.channel.send(f'Hello!! {message.author.name}')
        await message.channel.send("What's up, hope you are good")
        await message.channel.send('I can provide you with the most recent football⚽ data just by magic. Just follow my instruction to get that 😀')
        await message.channel.send("--------")
        await message.channel.send('* Type 1 to get the top 5 scores in the current league🥅\n* Type 2 to get Statistics about the most recent matches📊')
        await message.channel.send("--------")
    
    if message.content not in ['hello','1','2'] and message.author != client.user:
        await message.channel.send(f"{message.author.name} I don't understand, I only know football data. Type hello to discuss with me.")
        
    if message.content == '1':
        await message.channel.send(f' Yeah I know {message.author.name},try another option again. 😀')
    if message.content == '1':
        await message.channel.send(f'{message.author.name}, I am happy to serve you. 🖖')
        await message.channel.send(file=discord.File(football().visualize_command(1)))
    
    if message.content == '2':
        await message.channel.send(f'{message.author.name}, I am happy to serve you. 🖖')
        await message.channel.send(file=discord.File(football().visualize_command(2)))

    if message.content == '3':
        await message.channel.send(f'{message.author.name}, I am happy to serve you. 🖖')
        await message.channel.send(file=discord.File(football().visualize_command(3)))

    if message.content == '4':
        await message.channel.send(f'{message.author.name}, I am happy to serve you. 🖖')
        await message.channel.send(file=discord.File(football().visualize_command(4)))

client.run(TOKEN)

