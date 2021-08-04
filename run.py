from core import *
loadsetup = open('setting.txt', encoding='UTF8')
token = loadsetup.read()
loadsetup.close()
token = token[6:]
token = token[:-1]
try:
    startup(token)
except discord.errors.LoginFailure:
    print("로그인에 실패했어요 유효한 토큰이거나, 토큰에 큰 따옴표를 붙였는지 확인해주세요.")
    exit()