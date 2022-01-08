import discord
import sys
import os
sys.path.append(os.getcwd())
#from FinalProject.Data_Handling_tools.visualize import football
from FinalProject.Data_Handling_tools.visualize2 import football

##Personal information of the bit
TOKEN = ''
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
        await message.channel.send('* Type 1 to get the top 5 scores in the current league🥅\n'
        '* Type Lille to get the most recent statistics of "Lille" throughout wins, defeats and draws📊\n')
        await message.channel.send("--------")
    
    if message.content not in ['hello','1','2','3','4','5','6'] and message.author != client.user:
        await message.channel.send(f"{message.author.name} I don't understand, I only know football data. Type hello to discuss with me.")
        
    if message.content == 'cool':
        await message.channel.send(f' Yeah I know {message.author.name},try another option again. 😀')
    if message.content == '1':
        await message.channel.send(f'{message.author.name}, I am happy to serve you. 🖖')
        await message.channel.send(file=discord.File(football().visualize_command(1)))
    
    if message.content.lower() == 'lille':
        await message.channel.send(f'{message.author.name}, I am happy to serve you. 🖖')
        await message.channel.send(file=discord.File(football().visualize_command(2)))

    if message.content == '3':
        await message.channel.send(f'{message.author.name}, I am happy to serve you. 🖖')
        await message.channel.send(file=discord.File(football().visualize_command(3)))

    if message.content == '4':
        await message.channel.send(f'{message.author.name}, I am happy to serve you. 🖖')
        await message.channel.send(file=discord.File(football().visualize_command(4)))

client.run(TOKEN)

