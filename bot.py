# 匯入模組
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
import discord
import json
from discord.ext import commands
from pprint import pprint

# 設定 json 檔案路徑及程式操作範圍
Json = 'the-formula-307715-b90215218798.json'
Url = ['https://spreadsheets.google.com/feeds',
       'https://www.googleapis.com/auth/drive']

# 連線至資料表
Connect = SAC.from_json_keyfile_name(Json, Url)
GoogleSheets = gspread.authorize(Connect)

# 開啟資料表及工作表
Sheet = GoogleSheets.open_by_key('1UK4EJbukwoCWCneku3dFgwZ6OTx1zE11ECWXzh_wjMc')
Sheets = Sheet.worksheet('87BotTest')

#BOT 命令一定要以 / 作為開頭
bot = commands.Bot(command_prefix = '/')

#開啟token.json以讀取BOT的token
input_file = open ('token.json')
json_token = json.load(input_file)
for item in json_token :
    tokens = item['token']

#從google sheets讀取ID and Discord ID資料
Sheetsid = Sheet.worksheet('DiscordID對照表')
g8ids = Sheetsid.col_values(4)
b5ids = Sheetsid.col_values(2)
g8names = Sheetsid.col_values(3)
b5names = Sheetsid.col_values(1)


#BOT上線標記
@bot.event
async def on_ready():
    print(">> Bot is online <<")
    

#g8簽到命令
@bot.command()
async def g8sign(ctx , st):
    id = str(ctx.author.id)
    for i in range(len(g8ids)):
        if id == g8ids[i] : 
            point = i+10
            break
        else :
            continue
    
    print(point)
    cellg8 = 'F'+ str(point)

    await ctx.send(f'{g8names[point-10]}完成簽到 , {st}')
    Sheets.update_acell(cellg8,st)

#b5簽到命令
@bot.command()
async def b5sign(ctx , st):
    id = str(ctx.author.id)
    for i in range(len(b5ids)):
        if id == b5ids[i] : 
            point = i+12
            break
        else :
            continue
    
    print(point)
    cellb5 = 'E'+ str(point)

    await ctx.send(f'{b5names[point-12]}完成簽到 , {st}')
    Sheets.update_acell(cellb5,st)


#BOT執行
bot.run(tokens)
