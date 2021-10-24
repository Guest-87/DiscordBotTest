import discord
from discord.ext import commands

bot = commands.Bot(command_prefix = '[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

bot.run('OTAxODEwMzAxMTk5MDU2OTE2.YXVSSg.fSbFFVOSun6_xxydTl3hR8xC4Nk')