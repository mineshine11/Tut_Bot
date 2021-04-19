import discord
from discord.ext import commands


bot=commands.Bot(command_prefix='[')

@bot.event
async def on_ready():
    print(">> Bot is online <<")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(833753121288355922)
    await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
    channel = bot.get_channel(833753233490706462)
    await channel.send(f'{member} leave!')

bot.run("ODMzNzMwODU4MTM2ODk1NTI4.YH2mXg.tr-mKemjO8OKnAx673b970qTX40")