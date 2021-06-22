import discord, re, requests
from discord.ext import commands
from datetime import datetime
from bs4 import BeautifulSoup

class base(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.command(name="급식", help="군산 제일 고등학교의 급식을 표시합니다.", aliases=["밥"])
    #@commands.command()
    # aliases=["cmd1", "cmd2"]
    async def showlaunch(self, ctx):
        #await ctx.reply("Pong")
        no_num = re.compile('[^0-9]')
        res = requests.get ('https://search.naver.com/search.naver?sm=tab_hty.top&where=nexearch&query=%EA%B5%B0%EC%82%B0%EC%A0%9C%EC%9D%BC%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%90&oquery=%EA%B5%B0%EC%82%B0%EC%A0%9C%EC%9D%BC%EA%B3%A0%EB%93%B1%ED%95%99%EA%B5%A3&tqi=hZBadlp0J1ZssK9lMxNssssssrw-058069')
        source = res.text
        soup = BeautifulSoup(source,'html.parser')
        a = soup.select('.menu_info')
        menu = []
        dt = datetime.now()
        today = " "+str(dt.month)+"월 "+str(dt.day)+"일 "
        for menu in a:
            menu_today = menu.text[:menu.text.find('[')]
            if menu_today == today :
                replace1 = menu.text
                replace2 = replace1.replace("(정)","")
                replace3 = replace2.replace(".","")
                replace4 = "".join(no_num.findall(replace3))
                await ctx.send(replace4[4:])
def setup(bot):
    bot.add_cog(base(bot))