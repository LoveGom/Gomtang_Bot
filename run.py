from core import *
loadsetup = open('setting.txt', encoding='UTF8')
bwtoken = loadsetup.read()
loadsetup.close()
wtoken = bwtoken[5:]
try:
    startup(wtoken)
except discord.errors.LoginFailure:
    print("로그인에 실패했어요 토큰을 확인해주세요.")
