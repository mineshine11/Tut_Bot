import discord
from discord.ext import commands


bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

#bot.run("ODMzNzMwODU4MTM2ODk1NTI4.YH2mXg.tr-mKemjO8OKnAx673b970qTX40")