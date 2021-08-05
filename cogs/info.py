import discord, re, requests, psutil
from discord.ext import commands
class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="정보", help="현재 클라이언트의 정보를 표시합니다", aliases=["클", "온도"])
    async def showinfo(self, ctx):
        memory = psutil.virtual_memory()
        avail = round(memory.available/1024**3, 1) 
        percent = memory.percent 
        total = round(memory.total/1024**3, 1) 
        distotal = round(memory.total/1024**3) 
        embedVar = discord.Embed(title="정보", description="현재 클라이언트의 사용량을 표시합니다.", color=0x90EE90) 
        embedVar.add_field(name="CPU 사용량 :", value=f"{psutil.cpu_percent()}%", inline=False) 
        embedVar.add_field(name="메모리 사용량 :", value=f"{distotal}GB 중 {round(total - avail, 1)}GB 사용 중 ({avail}GB 사용 가능 ({percent}%))", inline=False)
        embedVar.set_thumbnail(url="https://i.imgur.com/73KqXFl.png#.YMmXoxXFi8U.link")
        await ctx.send(embed=embedVar) 
def setup(bot):
    bot.add_cog(base(bot))



