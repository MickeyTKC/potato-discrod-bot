#basic libs
import os
from dotenv import load_dotenv

#my libs
import fetch_data
from reports import sectors

#env setup
ENV = {
    "token": "potato_access_token"
}
#load .env file
load_dotenv()
#get values from .env
token = os.getenv(ENV['token'])

#discord bot setup
import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents = intents)
prefix = "!p."

#discord bot events
@client.event
# on discord bot ready
async def on_ready():
    print(f"目前登入身份 --> {client.user}")
    print("------")
    print("fetching data...")
    fetch_data.fetch_data()
    
#custom functions
async def ping(message):
    await message.channel.send("pong!")
    
async def fetching(message):
    fetch_data.fetch_data()
    await message.channel.send("Updating data...")
    
async def report(message):
    sectors.create()
    file = sectors.file_path
    await message.channel.send("近一年，美股行業報告", file=discord.File(file))

@client.event
# on new message arrived
async def on_message(message):
    # non bot message
    if message.author == client.user:
        return
    #if prefix is in message
    if message.content.startswith(prefix):
        #if command is !ping
        if message.content == prefix + "ping":
            await ping(message)
        if message.content == prefix + "fecth":
            await fetching(message)
        if message.content == prefix + "report.sectors":
            await report(message)
            
client.run(token)

