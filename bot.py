import discord
import random
import os
from dotenv import load_dotenv

load_dotenv()

TOKEN = os.getenv('DISCORD_TOKEN')

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

omikuji_list = ['大吉', '中吉', '小吉', '末吉', '凶']

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content == '!omikuji':
        result = random.choice(omikuji_list)
        await message.channel.send(f'🎋 おみくじ結果：{result} でした！')

client.run(TOKEN)
