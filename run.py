from core import *
loadsetup = open('setting.txt', encoding='UTF8')
token = loadsetup.read()
loadsetup.close()
rtoken = token.replace("토큰 : ", "").replace('"', "")
try:
    startup(rtoken)
except discord.errors.LoginFailure:
    print("로그인에 실패했어요 유효한 토큰이거나, 토큰에 큰 따옴표를 붙였는지 확인해주세요.")
    exit()