import discord
from discord.ext import commands
import datetime as dt
import random as rand
import time
import hashlib

vchannels = []
# vusers = []

cat_gif = ['https://tenor.com/view/kitty-highkitten-mdmacat-cat-happykitty-gif-6198981', 
'https://tenor.com/view/cat-meow-big-lips-gif-13233291', 
'https://tenor.com/view/smiling-cat-creepy-cat-cat-zoom-kitty-gif-12199043', 
'https://tenor.com/view/cats-whome-cute-awe-stare-gif-4004207', 
'https://tenor.com/view/lazy-cat-stairs-gif-13378074']

csoon = "That command is coming soon"

my_det = '''
Host OS: 
RAM: 
System Host IP: 
Host Manafatuer:
CPU: 
GPU: 
Storage:
The Bots Code is stored on Github.com
'''

cmds = '''
**help**: Displays This message

**users**: Displays the number of users in this server (including bots) (broken)

**yeet**: How could you yeet something so innocent

**cat**: Makes the bot send a random Gif of a cat

**fate**: Have your fait decided for you

**hello** or **hi**: makes the bot say Hello

**details**: shows details about the bots host

**say**: makes the bot say waht ever is put after the say command
'''

server_ids = {}
    

#open the file where the token is stored
o_token = open('token.txt', 'r')
token = o_token.read()
o_token.close()

bot = commands.Bot(command_prefix = '/')
bot.remove_command('help') #removes default help command

@bot.event
async def on_ready():
    #says its ready to go when its online
    Game = discord.Game('waiting for /help')
    await bot.change_presence(status=discord.Status.idle, activity = Game)
    print(f'logged on at: {dt.datetime.now()} and ready to go')
    

@bot.command()
async def test(ctx, *, testtex):
    await ctx.send(testtex)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello')

@bot.command()
async def hi(ctx):
    await ctx.send('Hello')

@bot.command()
async def help(ctx):
    embed1 = discord.Embed(titile = 'Help', description = 'Valid Commands', timestamp = dt.datetime.now())
    embed1.colour = discord.Colour.from_rgb(255,255,0)
    embed1.add_field(name = 'Prefix: /', value = cmds)
    embed1.set_thumbnail(url = 'https://www.models-resource.com/resources/big_icons/16/15871.png')
    await ctx.send(embed = embed1)

@bot.command()
async def details(ctx):
    embed2 = discord.Embed(titile = "Details", description = 'About my Host\'s', timestamp = dt.datetime.now())
    embed2.add_field(name = 'My Details', value = my_det)
    embed2.colour = discord.Colour.from_rgb(30,255,255)
    embed2.set_thumbnail(url = 'https://image.freepik.com/free-icon/view-details_318-1493.jpg')
    await ctx.send(embed = embed2)

@bot.command()
async def yeet(ctx):
    await ctx.send('https://tenor.com/view/yeet-rafiki-simba-lion-king-gif-12559094')

@bot.command()
async def cat(ctx):
        num = rand.randint(1, len(cat_gif) - 1)
        await ctx.send(cat_gif[num])

@bot.command()
async def fate(ctx):
        fs = [' Got Killed by a falling Minecraft Anvil', ' bled out from 28 stab wounds'] #the rest got removed so that they are special to the bot
        #num1 = rand.randint(1, len(fs) - 1)
        await ctx.send(f'{ctx.author.name}{rand.choice(fs)}')

@bot.command()
async def only_poop(ctx):
    await ctx.send('https://tenor.com/view/poop-shit-skateboard-tricks-cool-gif-16727878')

@bot.command()
async def say(ctx, *, sy1):
    await ctx.send(sy1)

@bot.command()
async def emoji(ctx):
    await ctx.send(':cat:')
    
@bot.command()
async def users(ctx):
    id = ctx.guild.id
    await ctx.send(f'Number of Users = {id.member_count}')

bot.run(token)
