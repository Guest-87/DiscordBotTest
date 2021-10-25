# 匯入模組
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
import discord
import json
from discord.ext import commands
from pprint import pprint

# 設定 json 檔案路徑及程式操作範圍
Json = 'the-formula-307715-a7b60e4ba970.json'
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

#開啟ID.json以讀取ID相關資料
# input_file = open ('ID.json')
# json_ID = json.load(input_file)
# for item in json_ID :
#     DCname = item['DCID']
#     name = item['ID']
#     point = item['point']


#BOT上線標記
@bot.event
async def on_ready():
    print(">> Bot is online <<")

#簽到命令
@bot.command()
async def sign(ctx , st):
    if ctx.author.name == '秋陽':
        point = 'F11'
    if ctx.author.name == '泡泡':
        point = 'F12'
    if ctx.author.name == '直美':
        point = 'F10'
    if ctx.author.name == 'Guest-87':
        point = 'F24'
    await ctx.send(f'{ctx.author.name}完成簽到 , {st}')
    Sheets.update_acell(point,st)

#BOT執行
bot.run(tokens)
