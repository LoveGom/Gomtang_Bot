import discord, re, requests, pybithumb
from discord.ext import commands
class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="시세", help="현재 주요 가상화폐의 시세를 확인합니다.", aliases=["빗", "비트코인", "코인"])
    #@commands.command()
    # aliases=["cmd1", "cmd2"]
    async def showcoin(self, ctx):
        embedVar = discord.Embed(color=0x00ff00) #embed 초기 설정을 합니다
        btc = pybithumb.get_current_price("BTC") #각 코인의 시세를 받아와서 서로의 이름의 변수에 넣습니다
        eth = pybithumb.get_current_price("ETH") #//
        xrp = pybithumb.get_current_price("XRP") #//
        embedVar.add_field(name="비트코인", value=f"{btc} BTC(₿)", inline=False) #embed에 각각 변수를 넣습니다
        embedVar.add_field(name="이더리움", value=f"{eth} ETH(Ξ)", inline=False) #//
        embedVar.add_field(name="리플", value=f"{xrp} XRP", inline=False) #//
        embedVar.set_thumbnail(url="https://i.imgur.com/73KqXFl.png#.YMmXoxXFi8U.link") #embed 썸네일을 지정합니다
        await ctx.send(embed=embedVar) #embed를 출력합니다
def setup(bot):
    bot.add_cog(base(bot))