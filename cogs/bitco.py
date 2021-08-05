import discord, re, requests, pybithumb
from discord.ext import commands
class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="시세", help="현재 주요 가상화폐의 시세를 확인합니다.", aliases=["빗", "비트코인", "코인"])
    async def showcoin(self, ctx):
        embedVar = discord.Embed(color=0x00ff00) 
        btc = pybithumb.get_current_price("BTC") 
        eth = pybithumb.get_current_price("ETH") 
        xrp = pybithumb.get_current_price("XRP") 
        embedVar.add_field(name="비트코인", value=f"{btc} BTC(₿)", inline=False) 
        embedVar.add_field(name="이더리움", value=f"{eth} ETH(Ξ)", inline=False)
        embedVar.add_field(name="리플", value=f"{xrp} XRP", inline=False) 
        embedVar.set_thumbnail(url="https://i.imgur.com/73KqXFl.png#.YMmXoxXFi8U.link") 
        await ctx.send(embed=embedVar) 
def setup(bot):
    bot.add_cog(base(bot))