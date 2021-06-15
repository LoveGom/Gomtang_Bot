import discord
from discord.ext import commands

class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="지연시간", help="봇의 클라이언트와 서버와의 지연시간을 계산합니다")
    #@commands.command()
    # aliases=["cmd1", "cmd2"]
    async def pingcmd(self, ctx):
        #await ctx.reply("Pong")
        await ctx.reply(f"Pong! {round(self.bot.latency * 1000)}ms")
def setup(bot):
    bot.add_cog(base(bot))