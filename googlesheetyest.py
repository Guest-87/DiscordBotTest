# 匯入模組
import gspread
from oauth2client.service_account import ServiceAccountCredentials as SAC

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

# 寫入資料
# dataTitle = ["會員 ID", "使用暱稱", "密碼"]
# datas = ["Captain", "Picard", "5678"]

# Sheets.append_row(dataTitle)
# Sheets.append_row(datas)
# print("寫入成功")
Sheets.update_acell('F10','七點半前集合')
Sheets.update_acell('F11','八點前集合')
Sheets.update_acell('F12','領土戰期間會出現')
Sheets.update_acell('F13','不一定出現')
Sheets.update_acell('F14','無法參加')
Sheets.update_acell('F15','???')
# 讀取資料
print(Sheets.get_all_values())

