import discord
import logging
import secret.token

TOKEN = secret.token.get_token()
client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)

shadow_realm = None
ander = 140901403592884224
wokanoga = 81423485208891392


@client.event
async def on_connect():
    print('Connected\nLogging in\n')


@client.event
async def on_ready():
    print('Logged in as {0.user}, ID {0.user.id}'.format(client))
    print('Ready to B.A.N\n')
    global shadow_realm
    shadow_realm = discord.utils.get(client.get_all_channels(), id=306630991018065932)


@client.event
async def on_message(message):
    # on_message fires on EVERY message in every channel that the bot is in.  Including dms.
    if message.author == client.user:
        return
    elif message.content == 'bpTest':
        print(get_user(wokanoga))
    elif message.content == 'bpTest ban all':
        that_cheese_members = discord.utils.get(client.get_all_channels(), id=153306465367490560).members
        print('Message Event ran')
        await ban_all(that_cheese_members)
    elif message.content == 'B.A.N Ander':
        user = get_user(ander)
        if user is None:
            return
        else:
            await user.move_to(shadow_realm, reason=None)
    elif message.content == 'B.A.N Ander a lot':
        user = get_user(ander)
        if user is None:
            return
        else:
            print('ban ander a lot')


async def ban_all(members):
    # I might want to make this go through all my channels and not just the one sent.
    for member in members:
        await member.move_to(shadow_realm, reason=None)


async def ban_user(member):
    await member.move_to(shadow_realm, reason=None)


async def get_user(id_number):
    return discord.utils.get(client.get_all_members(), id=id_number)


client.run(TOKEN)
