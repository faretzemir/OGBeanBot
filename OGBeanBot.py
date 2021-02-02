# This program is the OGBeanBot
import discord
TOKEN = '...'
from random import randrange
client = discord.Client()

reply1 = "Hello uwu owo!"
reply2 = "Yeah mate, what's going on?"
reply3 = "Yes it's me the OG Bean Bot."
reply4 = "Let's play Minceraft together!"
reply5 = 'Notto disu shitto agen.'
reply6 = 'Type "!OGhelp" for help on bot commands.'

print('Starting bot...')

@client.event
async def on_ready():
    print('Logged in as')
    print(client.user.name)
    print(client.user.id)
    print('------')
    print('Bot online and operational.')
    print('DO NOT CLOSE THIS WINDOW.')

def is_me(m):
    return m.author == client.user

nl = '\n'

@client.event
async def on_message(message):
    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    elif message.content.startswith('!hello'):
        msg = 'Hello, {0.author.mention}. \nThe weather today is (!great/!shit) [choose one].'.format(message)
        await message.channel.send(msg)

    elif message.content.startswith('!shit'):
        msg = "Awww that's a shame..."
        await message.channel.send(msg)

    elif message.content.startswith('!great'):
        msg = "That's great to hear uwu!"
        await message.channel.send(msg)

    elif message.content.startswith('!bemygf'):
        msg = "No."
        await message.channel.send(msg)

    elif message.content.startswith('!OGdelete'):
        await message.channel.purge(limit=50, check=is_me)


    elif message.content.startswith('!welcome'):
        msg = 'Welcome, {0.author.mention} to the Cool Beans Server. \n\nChat with other beans in the Forum for text, and the Penthouse for voice chat.'.format(message)
        msg1 = '\nWe have also a Minecraft server which we play on. \n\nThere is a bot that notifies the Discord server upon turning on. \nThe address is: CoolBeansServer2.aternos.me'
        msg2 = '\n\nType "!OGhelp" for help on commands.'
        await message.channel.send(msg + nl + msg1 + msg2)
        
    elif message.content.startswith('!OGhelp'):
        comms = 'The OGBeanBot can do the following:'
        msg = '\nType "!hello" to say hello.'
        msg1 = '\n\nType "!welcome" for a welcome message and some information.'
        msg2 = '\n\nType "!OGhelp" for help on commands. \n\nYou can also mention the bot for fun.'
        msg3 = '\n\nType "!goodnight" to say goodnight to OG.'
        msg4 = '\n\nType "!rick for a link to Never Gonna Give You Up.'
        msg5 = '\n\nType "!najib" for a good laugh.'
        msg6 = '\n\nType "!mcserverinfo" or "!mcinfo" for information on our Minecraft Java Server!'
        msg7 = '\n\n Type "!phonetic" for a Phonetic Alphabet chart. (Helps when spelling out words over discord when the connection is unstable)'
        await message.channel.send(comms + msg + msg1 + msg2 + msg3 + msg4 + msg5 + msg6 + msg7)

    elif message.content.startswith('!goodnight'):
        msg = 'Goodnight, {0.author.mention}! Sweet dreams!'.format(message)
        await message.channel.send(msg)

    elif message.content.startswith('!rick'):
        msg = 'https://www.youtube.com/watch?v=dQw4w9WgXcQ'
        await message.channel.send(msg)

    elif message.content.startswith('!najib'):
        i = randrange(5)

        if (i==0):
            najib = discord.File("najib.jpeg", filename="najib.jpeg")
            embed = discord.Embed()
            embed.set_image(url="attachment://najib.jpeg")
            await message.channel.send(file=najib, embed=embed)
        elif (i==1):
            najib = discord.File("najib1.PNG", filename="najib.PNG")
            embed = discord.Embed()
            embed.set_image(url="attachment://najib.PNG")
            await message.channel.send(file=najib, embed=embed)
        elif(i==2):
            najib = discord.File("najib2.jpg", filename="najib2.jpg")
            embed = discord.Embed()
            embed.set_image(url="attachment://najib2.jpg")
            await message.channel.send(file=najib, embed=embed)
        elif(i==3):
            najib = discord.File("najib3.jpg", filename="najib3.jpg")
            embed = discord.Embed()
            embed.set_image(url="attachment://najib3.jpg")
            await message.channel.send(file=najib, embed=embed)
        elif(i==4):
            najib = discord.File("najib4.PNG", filename="najib4.PNG")
            embed = discord.Embed()
            embed.set_image(url="attachment://najib4.PNG")
            await message.channel.send(file=najib, embed=embed)
        
        i = randrange(5)
        

    elif message.content.startswith('!phonetic'):
        phonetic = discord.File("phonetic.jpg", filename="phonetic.jpg")
        embed = discord.Embed()
        embed.set_image(url="attachment://phonetic.jpg")
        await message.channel.send(file=phonetic, embed=embed)

    elif message.content.startswith('!mcserverinfo') or message.content.startswith('!mcinfo'):
        msg = '\nServer address: CoolBeansServer2.aternos.me'
        msg1 = '\nHosting website: https://aternos.org/servers/'
        await message.channel.send(msg + msg1)
 
    elif client.user.mentioned_in(message) and message.mention_everyone is False:
        i = randrange(6)
        
        if (i == 0):
             await message.channel.send(reply1)
        elif (i == 1):
            await message.channel.send(reply2)
        elif (i == 2):
            await message.channel.send(reply3)
        elif (i == 3):
            await message.channel.send(reply4)
        elif (i == 4): 
            await message.channel.send(reply5)
        elif (i == 5):
            await message.channel.send(reply6)

        i = randrange(6)
        

client.run(TOKEN)