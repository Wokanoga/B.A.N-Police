import discord
import logging
from discord.ext import commands
TOKEN = 'Njc0MDA1Njg2MjM3MDAzNzk3.XjiV_w.6D0VW1d92YVtMBCeY4dFWvJGya8'
client = discord.Client()

logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)


@client.event
async def on_ready():
    print('Logged in as {0.user}, ID {0.user.id}'.format(client))
    # print(client.user.name)
    # print(client.user.id)
    print('------')


@client.event
async def on_message(message):
    # on_message fires on EVERY message in every channel that the bot is in.  Including dms.
    if message.author == client.user:
        return
    elif message.content.startswith('B.A.N'):
        msg = 'Hello {0.author.mention}'.format(message)
        await message.channel.send(msg)


client.run(TOKEN)
