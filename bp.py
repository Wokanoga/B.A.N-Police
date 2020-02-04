import discord
import logging
import secret.token

TOKEN = secret.token.get_token()
client = discord.Client()
print(TOKEN)
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
    wokanoga = discord.utils.get(client.get_all_members(), id=81423485208891392)
    shadow_realm_members = discord.utils.get(client.get_all_channels(), id=306630991018065932).members
    print(shadow_realm_members)
    print(True) if wokanoga in shadow_realm_members else print(False)


@client.event
async def on_message(message):
    # on_message fires on EVERY message in every channel that the bot is in.  Including dms.
    if message.author == client.user:
        return
    # elif message.content.startswith('B.A.N'):
    elif message.content == 'bpTest':
        print('bpTest')
    elif message.content == 'bpTest ban all':
        that_cheese_members = discord.utils.get(client.get_all_channels(), id=153306465367490560).members
        print('Message Event ran')
        await ban_all(that_cheese_members)
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
    # group is not voice.  Fuck.
    print('Event ran')
    shadow_realm = discord.utils.get(client.get_all_channels(), id=306630991018065932)
    if channel is shadow_realm:
        print(f'User {user}, joined a channel that was not the Shadow Realm')
    else:
        print(f'User {user}, was banished to the Shadow Realm')


async def ban_all(members):
    # I might want to make this go through all my channels and not just the one sent.
    for member in members:
        print(f'ban {member}')


client.run(TOKEN)
