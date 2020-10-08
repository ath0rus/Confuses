import discord
import datetime as dt
import random as rand
import time

vchannels = ['1a', '2a', '💬-general', '🤖bot-commands-and-stuff']
# vusers = ['ath0rus#2069', 'wallGraffiti#5365', 'phos#4938']

cat_gif = ['https://tenor.com/view/kitty-highkitten-mdmacat-cat-happykitty-gif-6198981', 'https://tenor.com/view/cat-meow-big-lips-gif-13233291', 'https://tenor.com/view/smiling-cat-creepy-cat-cat-zoom-kitty-gif-12199043', 'https://tenor.com/view/cats-whome-cute-awe-stare-gif-4004207', 'https://tenor.com/view/lazy-cat-stairs-gif-13378074']

csoon = "That command is coming soon"

# help_me = '''
# Bellow you find a List of commands and also some details about the system that host's me
# '''

my_det = '''
Host OS: Windows 10 (2004)
RAM: 8GB DDR3 or 12GB DDR4
System Host IP: ||Nope||
Host Manafatuer: Dell Desktop or Acer Laptop
CPU: i5 8250U
GPU: MX130 (deicated) or Intel HD Graphics
Storage: 1TB samsung EVO SSD or LITEON 256GB SSD
The Bots Code is stored on Github.com
'''

cmds = '''
**help**: Displays This message

**memebers**: Displays the number of Members in this server (including bots)

**yeet**: How could you yeet somrthing so innocent

**cat**: Makes the bot send a random Gif of a cat

**fait**: Have your fait decided for you (WIP)

**pain**: makes the bot become a pain in the ass for a few seconds (5 times only)
'''

server_ids = {
    #BT(oym)
    "bt": 715493968921493614,
    #Cordless Cat
    "cc": 678543198846713861,
    #Salt
    "slt": 339355554084290560,
    }

#open the file where the token is stored
o_token = open('token.txt', 'r')
token = o_token.read()
o_token.close()

client = discord.Client()

@client.event
async def on_ready():
    print(f'logged on at: {dt.datetime.now()} and ready to go')
    Game = discord.Game('waiting for /help')
    await client.change_presence(status=discord.Status.idle, activity = Game)

@client.event
async def on_message(msg):
    # print(msg.content, )
    id = client.get_guild(server_ids["cc"])

    #if str(msg.channel) in vchannels:
        
        # if msg.content.find('hello') != -1:
        #     await msg.channel.send('hi')

    if msg.content == 'Hello':
        await msg.channel.send('HI!')

    elif msg.content == 'hello':
        await msg.channel.send('HI!')

    elif msg.content == 'hi':
        await msg.channel.send("HELLO!")

    elif msg.content == 'Hi':
        await msg.channel.send("HELLO!")
        
    elif msg.content == '/members':
        await msg.channel.send(f'# of memebers: {id.member_count}')
        
    elif msg.content == '/help':
        embed1 = discord.Embed(titile = 'Help', description = 'Valid Commands', timestamp = dt.datetime.now())
        embed1.colour = discord.Colour.from_rgb(255,255,0)
        embed1.add_field(name = 'Prefix: /', value = cmds)
        embed1.set_thumbnail(url = 'https://www.models-resource.com/resources/big_icons/16/15871.png')
        await msg.channel.send(embed = embed1)

    elif msg.content == '/details':
        embed2 = discord.Embed(titile = "Details", description = 'About my Host\'s', timestamp = dt.datetime.now())
        embed2.add_field(name = 'My Details', value = my_det)
        embed2.colour = discord.Colour.from_rgb(30,255,255)
        embed2.set_thumbnail(url = 'https://image.freepik.com/free-icon/view-details_318-1493.jpg')
        await msg.channel.send(embed = embed2)

    elif msg.content == '/yeet':
        await msg.channel.send('https://tenor.com/view/yeet-rafiki-simba-lion-king-gif-12559094')

        # elif msg.content == 'yeet':
        #     await msg.channel.send('https://tenor.com/view/yeet-rafiki-simba-lion-king-gif-12559094')

    elif msg.content == '/cat':
        num = rand.randint(1, len(cat_gif) - 1)
        await msg.channel.send(cat_gif[num])

    elif msg.content == '/fait':
        fs = [' Got Killed by a falling Minecraft Anvil', ' bled out from 28 stab wounds', ' Was eaten to bits by Chonke Kittens', ' Fell off a sky scraper', ' Stayed up for too long and died from sleep deprivation', ' Bled oyt from a DEEEEEP paper cut', ' Spent to much time watching Juicy and drank Paint', ' Decided to play Dumb Ways to Die IRL and never got saved']
        #num1 = rand.randint(1, len(fs) - 1)
        await msg.channel.send(f'{msg.author.name}{rand.choice(fs)}')

    elif msg.content == '/only poop':
        await msg.channel.send('https://tenor.com/view/poop-shit-skateboard-tricks-cool-gif-16727878')

    elif msg.content == '/pain':
        for i in range(5):
            await msg.channel.send('YEET!!')
            # time.sleep(5)
            # for i in range(5):
            #     await msg.channel.send('YEET!!')

    elif msg.content.startswith == "Simon says":
        await msg.channel.send(msg.content)
        print(msg.content)

    elif msg.content.startswith == "/tableflip ":
        await msg.channel.send('┬─┬ ノ( ゜-゜ノ)')

@client.event
async def on_memeber_join(member):
    for channel in member.guild.channels:
        if str(channel) == "welcomes":
            await channel.send_message(f'Welcome to the server {member.mention}')


client.run(token)