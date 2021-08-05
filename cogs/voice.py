import discord
from discord.ext import commands
class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="emote", help="케인인님의 임티를 보낸다맨이야!", aliases=["임", "임티"])
    async def emote(self, ctx, *, emote):
        pass

def setup(bot):
    bot.add_cog(base(bot))