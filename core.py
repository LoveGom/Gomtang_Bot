import discord, asyncio, os
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix="곰탱쓰 ", intents=discord.Intents.all())

for cogs in os.listdir("cogs"):
    if cogs.endswith(".py"):
        bot.load_extension(f"cogs.{cogs[:-3]}")
        print(f"cogs.{cogs[:-3]}을 성공적으로 로드했어요!")
@bot.event
async def on_ready():
    print(f"loggin {bot.user.name}")
    date = datetime.now()
    while(True):        
        await bot.change_presence(activity = discord.Streaming(name = "gt.도움", url= "https://www.twitch.tv/bookguk_gom")) #디스코드 rich presence
        await asyncio.sleep(5)
        await bot.change_presence(activity = discord.Streaming(name = f"ver. BATA {date.year}. {date.month}. {date.day}. ", url= "https://www.twitch.tv/bookguk_gom"))
        await asyncio.sleep(5)



def startup(token):
    bot.run(token)