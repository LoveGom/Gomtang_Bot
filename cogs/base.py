import discord
from discord.ext import commands

bot = commands.Bot(command_prefix="!", intents=discord.Intents.all())

class base(commands.Cog, name="일반"):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="ping", help="봇의 클라이언트와 서버와의 지연시간을 계산합니다")
    # aliases=["cmd1", "cmd2"]
    async def pingcmd(self, ctx):
        #await ctx.reply("Pong")
        await ctx.reply(f"Pong! {round(bot.latency * 1000)}ms")
def setup(bot):
    bot.add_cog(base(bot))