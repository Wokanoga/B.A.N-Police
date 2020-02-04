import discord
import logging
from discord.ext import commands

TOKEN = 'Njc0MDA1Njg2MjM3MDAzNzk3.Xji2Gw.z0b6wHFaDrhLnUtV7labVGtNPjA'
client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@client.event
async def on_connect():
    print('Connected\nLogging in\n')


@client.event
async def on_ready():
    print('Logged in as {0.user}, ID {0.user.id}'.format(client))
    print('Ready to B.A.N\n')
    that_cheese = discord.utils.get(client.get_all_channels(), id=153306465367490560)
    # print(client.user.name)
    # print(client.user.id)
    # -------------------------------------------------------------
    # my id
    # user = discord.utils.get(client.get_all_members(), id=81423485208891392)
    # Anders id
    # user = discord.utils.get(client.get_all_members(), id=140901403592884224)
    # print(f'Target user is {user}')
    # if user is None:
    #     return
    # else:
    #     await user.send("A message for you")


@client.event
async def on_message(message):
    # on_message fires on EVERY message in every channel that the bot is in.  Including dms.
    if message.author == client.user:
        return
    # elif message.content.startswith('B.A.N'):
    elif message.content == 'B.A.N Ander':
        user = discord.utils.get(client.get_all_members(), id=81423485208891392)
        shadow_realm = discord.utils.get(client.get_all_channels(), id=306630991018065932)
        if user is None:
            return
        else:
            print('Gotta move the user here')
        msg = 'You\'re fucking banned. {0.author.mention}'.format(message)
        await message.channel.send(msg)


@client.event
async def on_group_join(channel, user):
    print('Event ran')
    shadow_realm = discord.utils.get(client.get_all_channels(), id=306630991018065932)
    if channel is shadow_realm:
        print(f'User {user}, joined a channel that was not the Shadow Realm')
    else:
        print(f'User {user}, was banished to the Shadow Realm')


client.run(TOKEN)
