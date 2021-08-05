import discord
from discord.ext import commands

class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="emote", help="케인인님의 임티를 보낸다맨이야!", aliases=["임", "임티"])
    async def emote(self, ctx, *, emote):
        if emote == "뭉탱이":
            await ctx.message.delete()
            await ctx.send("||**뭉탱이로 있다가 유리게슝으로 아니 그냥...**||")
            await ctx.send("https://media1.tenor.com/images/b33729273350e4dbddcc47e3fe7a0093/tenor.gif?itemid=19912401")
        elif emote == "무빙맨":
            await ctx.message.delete()
            await ctx.send("||**무빙맨**||")
            await ctx.send("https://media1.tenor.com/images/094b85c3701fcc1343d864d4c193ce10/tenor.gif?itemid=22562133")
        elif emote == "바선생":
            await ctx.message.delete()
            await ctx.send("https://media.tenor.com/images/a9ca502195c292a122b0475c3ed48154/tenor.gif")
        else:
            await ctx.send("얘! 그런 임티는 없단다!")
        

def setup(bot):
    bot.add_cog(base(bot))