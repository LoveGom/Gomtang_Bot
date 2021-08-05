import discord
from discord.ext import commands

class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="지연시간", help="봇의 클라이언트와 서버와의 지연시간을 계산합니다", aliases=["지연", "핑"])
    async def pingcmd(self, ctx):
        await ctx.reply(f"Pong! {round(self.bot.latency * 1000)}ms")
    @commands.command(name="도움", aliases=["도움말", "헬프"])
    async def helpembed(self, ctx):
        embedVar = discord.Embed(title="도움말", description="명령어는 아래에서 확인하세요!", color=0x00ff00) 
        embedVar.add_field(name=f"곰탱쓰 지연시간", value="네트워크 지연시간을 표기합니다.", inline=False)
        embedVar.add_field(name=f"곰탱쓰 시세", value="비트코인 시세를 확인합니다.", inline=False)
        embedVar.add_field(name=f"곰탱쓰 정보", value="현재 돌아가고 있는 서버의 상태를 확인합니다.", inline=False)
        embedVar.add_field(name=f"곰탱쓰 급식", value="군산 제일고등학교의 급식을 확인합니다.", inline=False)
        embedVar.add_field(name=f"곰탱쓰 이모티콘", value="미리 저장된 gif 이미지를 전송합니다.", inline=False)
        embedVar.set_thumbnail(url="https://i.imgur.com/73KqXFl.png#.YMmXoxXFi8U.link") 
        await ctx.send(embed=embedVar) 

def setup(bot):
    bot.add_cog(base(bot))