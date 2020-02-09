import discord
import logging
import time
import re
import secret.token

TOKEN = secret.token.get_token()
client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

black_list = []
white_list = []
ander = 140901403592884224
wokanoga = 81423485208891392


@client.event
async def on_connect():
    print('Connected\nLogging in\n')


@client.event
async def on_ready():
    print('Logged in as {0.user}, ID {0.user.id}'.format(client))
    print('Ready to B.A.N\n')


@client.event
async def on_message(message):
    if message.author == client.user or message.content.startswith('B.A.N') is not True:
        return
    elif message.content.endswith('fuck'):
        print(True)
    elif message.content == 'B.A.N All':
        for channel in message.guild.voice_channels:
            if channel is not message.guild.afk_channel:
                await ban_all_users(message.guild, channel.members)
    elif message.content.startswith('B.A.N <@!'):
        user_id = int(re.search(r'[0-9]+', message.content).group())
        user = await get_user(user_id)
        print(user)
        if user is None or user == client.user:
            return
        else:
            await user.move_to(message.guild.afk_channel, reason=None)
    elif message.content == 'B.A.N Ander a lot':
        user = await get_user(ander)
        if user is None or user in black_list:
            return
        else:
            user.move_to(message.guild.afk_channel, reason=None)
            black_list.append(user)
            time.sleep(10)
            black_list.remove(user)
    elif message.content.startswith('B.A.N perma'):
        user = get_user(ander)
        if user is None:
            return
        else:
            print('fuck')


@client.event
async def on_voice_state_update(member, before, after):
    # print(f'{member}\n{before}\n{after}\n')
    if member in black_list:
        print(member)


async def ban_all_users(guild, members):
    for member in members:
        await member.move_to(guild.afk_channel, reason=None)


async def ban_user(guild, member):
    await member.move_to(guild.afk_channel, reason=None)


async def get_user(arg):
    return discord.utils.get(client.get_all_members(), id=arg)


client.run(TOKEN)
