import discord
from discord.ext import commands
import datetime as dt
import random as rand
import time
import hashlib

vchannels = ['1a', '2a', '💬-general', '🤖bot-commands-and-stuff']
# vusers = ['ath0rus#2069', 'wallGraffiti#5365', 'phos#4938']

cat_gif = ['https://tenor.com/view/kitty-highkitten-mdmacat-cat-happykitty-gif-6198981', 
'https://tenor.com/view/cat-meow-big-lips-gif-13233291', 
'https://tenor.com/view/smiling-cat-creepy-cat-cat-zoom-kitty-gif-12199043', 
'https://tenor.com/view/cats-whome-cute-awe-stare-gif-4004207', 
'https://tenor.com/view/lazy-cat-stairs-gif-13378074']

csoon = "That command is coming soon"

my_det = '''
Host OS: Windows 10 (2004)
RAM: 12GB DDR4
System Host IP: ||Nope||
Host Manafatuer:Acer Laptop
CPU: i5 8250U
GPU: MX130 (deicated) or Intel HD Graphics
Storage: 1TB samsung EVO SSD or LITEON 256GB SSD
The Bots Code is stored on Github.com
'''

cmds = '''
**help**: Displays This message

**users**: Displays the number of users in this server (including bots)

**yeet**: How could you yeet something so innocent

**cat**: Makes the bot send a random Gif of a cat

**fate**: Have your fait decided for you

**hello** or **hi**: makes the bot say Hello

**details**: shows details about the bots host

**say**: makes the bot say waht ever is put after the say command
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
        fs = [' Got Killed by a falling Minecraft Anvil', ' bled out from 28 stab wounds', ' Was eaten to bits by Chonky Kittens', ' Fell off a sky scraper', 
        ' Stayed up for too long and died from sleep deprivation', ' Bled out from a DEEEEEP paper cut', ' Spent to much time watching Juicy and drank Paint', 
        ' Decided to play Dumb Ways to Die IRL and never got saved', ' Trusted the imposter', ' Got voted off for calling an emergency meeting to say "Hi"',
        ' Suffocated by a Fur ball', ' Miscalcualted a dive off a 80 foot (24.384m) cliff', ' Danced near molten lava and fell in', ' Picked a fight with Elsa',
        ' Thought they ran the animal Kingdom', ' Ignored rairoad crossing signals', ' Took the vending machine challenge', ' Was a distracted driver', ' shopped on black friday', 
        ' Forgot how to breathe', ' Drove off of a cliff but survive but die of shock from the high price of their hospital bill', ' Listened to Justin Beiber for Too Long',
        ' Drowned in Jell-o (jelly)', ' Tryed to eat a whole Big Mac in one bite and chocked to death', ' Chocked on their own tongue (Actually possible)', ' Got their face caught in an egg beater',
        ' Tryed to fly off a building', ' Drank too much anti-Freeze', ' Got their head ripped off by an elevator', ' got stuck in a tanning booth', ' Walked across quicksand while carrying an anvil',
        ' set fire to their own hair', ' Tryed to catch a piranha with their own tongue', ' Got stabbed with a cucumber', ' Poked a stick at a grizzly bear', 
        ' Their teacher Gave them ten tons of homework, and their brain exploded', ' Took their helmet off in outer space and their head explodes they froze to death', ' Played Russian Roulette with a fully loaded Uzi']
        #num1 = rand.randint(1, len(fs) - 1)
        await ctx.send(f'{ctx.author.name}{rand.choice(fs)}')

@bot.command()
async def only_poop(ctx):
    await ctx.send('https://tenor.com/view/poop-shit-skateboard-tricks-cool-gif-16727878')

@bot.command()
async def say(ctx, *, sy1):
    await ctx.send(sy1)

# @bot.command()
# async def (╯°□°）╯︵ ┻━┻ (ctx):
#     await ctx.send('"That is Illegal Sir" - Hollis\n/unflip')

@bot.command()
async def emoji(ctx):
    await ctx.send(':cat:')
    
@bot.command()
async def users(ctx):
    id = ctx.guild.id
    await ctx.send(f'Number of Users = {id.member_count}')

bot.run(token)