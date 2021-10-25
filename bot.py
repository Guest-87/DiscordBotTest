
import discord
import json
from discord.ext import commands

bot = commands.Bot(command_prefix = '[')
input_file = open ('token.json')
json_token = json.load(input_file)
for item in json_token :
    tokens = item['token']
@bot.event
async def on_ready():
    print(">> Bot is online <<") 

bot.run(tokens)