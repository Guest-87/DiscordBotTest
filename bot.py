# 匯入模組
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC
import discord
import json
import datetime
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
Sheetg8 = Sheet.worksheet('姬掰簽到表')
Sheetb5 = Sheet.worksheet('天下布武簽到')

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

    if   st == '730' :
        await ctx.send(f'{g8names[point-10]}完成簽到 , 七點半前集合')
        Sheetg8.update_acell(cellg8,'七點半前集合')
    elif st == '800' :
        await ctx.send(f'{g8names[point-10]}完成簽到 , 八點前集合')
        Sheetg8.update_acell(cellg8,'八點前集合')
    elif st == 'doing' :
        await ctx.send(f'{g8names[point-10]}完成簽到 , 領土戰期間會出現')
        Sheetg8.update_acell(cellg8,'領土戰期間會出現')
    elif st == 'unknow' :
        await ctx.send(f'{g8names[point-10]}完成簽到 , 不一定出現')
        Sheetg8.update_acell(cellg8,'不一定出現')
    elif st == 'no' :
        await ctx.send(f'{g8names[point-10]}完成簽到 , 無法參加')
        Sheetg8.update_acell(cellg8,'無法參加')
    else : 
        await ctx.send('請按照格式輸入指令')

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

    if   st == '730' :
        await ctx.send(f'{b5names[point-12]}完成簽到 , 七點半前集合')
        Sheetb5.update_acell(cellb5,'七點半前集合')
    elif st == '800' :
        await ctx.send(f'{b5names[point-12]}完成簽到 , 八點前集合')
        Sheetb5.update_acell(cellb5,'八點前集合')
    elif st == 'doing' :
        await ctx.send(f'{b5names[point-12]}完成簽到 , 領土戰期間會出現')
        Sheetb5.update_acell(cellb5,'領土戰期間會出現')
    elif st == 'unknow' :
        await ctx.send(f'{b5names[point-12]}完成簽到 , 不一定出現')
        Sheetb5.update_acell(cellb5,'不一定出現')
    elif st == 'no' :
        await ctx.send(f'{b5names[point-12]}完成簽到 , 無法參加')
        Sheetb5.update_acell(cellb5,'無法參加')
    else : 
        await ctx.send('請按照格式輸入指令')

#Tag未簽到人員
@bot.command()
async def nosign(ctx):
    g8no = Sheetg8.col_values(6)
    b5no = Sheetb5.col_values(5)
    g8ids = Sheetsid.col_values(4)
    b5ids = Sheetsid.col_values(2)
    allnog8 = ''
    allnob5 = ''
    #print(g8no)
    for i in range(len(g8ids)) :
        print(i+11) 
        if g8no[i+10] == '' : 
            allnog8 = allnog8+'<@!'+g8ids[i]+'>'
            if i%30==29 : 
                await ctx.send(f'{allnog8} , 請去簽到 , 謝謝 。')
                allnog8 = '' 
        else : 
            continue
    await ctx.send(f'{allnog8} , 請去簽到 , 謝謝 。')

    for i in range(len(b5ids)) :
        print(i+12) 
        if b5no[i+12] == '' : 
            allnob5 = allnob5+'<@!'+b5ids[i]+'>'
            if i%30==29 : 
               await ctx.send(f'{allnob5} , 請去簽到 , 謝謝 。')
               allnob5 = ''
        else : 
            continue
    
    await ctx.send(f'{allnob5} , 請去簽到 , 謝謝 。')
    
    print('finish')

#清空簽到表and自動更換日期
@bot.command()
async def nextweek(ctx):
    g8day  =  Sheetg8.acell('C8').value
    g8week =  Sheetg8.acell('D8').value
    g8days = datetime.datetime.strptime(g8day, "%Y/%m/%d")
    print(datetime.datetime.date(g8days))
    fourday = datetime.timedelta(days=4)
    threeday = datetime.timedelta(days=3)

    if g8week == '星期二' : 
        addday = fourday
        week = '星期六'
    elif g8week == '星期六' : 
        addday = threeday
        week = '星期二'

    alldate = g8days + addday

    Sheetg8.update_acell('C8',f'{alldate.strftime("%Y/%m/%d")}')
    Sheetb5.update_acell('A10',f'{alldate.strftime("%Y/%m/%d")}')
    Sheetg8.update_acell('D8',f'{week}')
    Sheetb5.update_acell('D10',f'{week}')
    print(alldate.strftime("%Y/%m/%d"))
    g8row = Sheetg8.range("F10:F109")
    b5row = Sheetb5.range("E12:E111")
    for cell in g8row:
        cell.value = ''
    for cell in b5row:
        cell.value = ''
    Sheetg8.update_cells(g8row)
    Sheetb5.update_cells(b5row)
    

#BOT執行
bot.run(tokens)
