import discord
from discord.ext import commands
class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="voice", help="voice chat", aliases=["음", "음챗"])
    async def voice(self, ctx):
        pass

def setup(bot):
    bot.add_cog(base(bot))