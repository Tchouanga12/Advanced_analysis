import discord

##Personal information of the bit
TOKEN = 'OTE4MTY2NDU2NzQ5OTIwMzQ2.YbDTJQ.W_T-j0P45W9UgOmqt1n-OUFfdMA '
##Doscird channel also know as guild
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
        f'{guild.name}(id: {guild.id})'
    )

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
        
    if message.content in ['1','2']:
        await message.channel.send(f'{message.author.name} the content is not yet available come back soon 🖖')

client.run(TOKEN)

