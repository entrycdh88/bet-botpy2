import asyncio
import discord
import os
import random
vspl = message.content.split(' ')

client = discord.Client()
token = os.environ["BOT_TOKEN"]
prefix = "off"
@client.event
async def on_ready():
    print("Logged in as ")
    print(client.user.name)
    print(client.user.id)
    print("===========")
    await client.change_presence(game=discord.Game(name="Github 호스팅중", type=1))
    print('Logged bot')
@client.event
async def on_message(message):
    if message.author.bot:
        return None

    if message.content == '쌀국수':
        await message.channel.send('뚝배기')

    if message.content == '랩터':
        await message.channel.send('이슬찬 (ft.proyoutuber)')

    if message.content == '에임갓':
        await message.channel.send('이주환 (반대로 하면 에임ㄸ)')

    if message.content == 'dju20026':
        await message.channel.send('임정준 (쭌)')
client.run(token)
