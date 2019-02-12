import gspread
from oauth2client.service_account import ServiceAccountCredentials

scope = ['http://spreadsheets.google.com/feeds', 'https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('C:/Users/Andrew/Downloads/GoogleSheetsPG-0eba919971ef.json',
                                                         scope)
client = gspread.authorize(creds)
sheet = client.open('test_py').sheet1

# print(sheet.get_all_records())

cell_number_with_C = 8
cell_check = 9
row_check = 1
cell_new = 10
col_with_c_len = sheet.col_values(cell_number_with_C).__len__() + 1
cshki = 'C'
CforTasks = []
thiset = {}

print(sheet.col_values(1).sort()+'\n')

for i in range(1, col_with_c_len):
    if (sheet.cell(i, cell_number_with_C).value.__contains__('C') or sheet.cell(i, cell_number_with_C).value.__contains__('c') ) and sheet.cell(i, cell_check).value.__contains__('Task'):
                while sheet.cell(i, cell_check).value == sheet.cell(i+1, cell_check).value:
                    cshki =+ sheet.cell(i, cell_number_with_C).value
                    sheet.update_cell(i, cell_new, 'Покрыть проверки: ' + cshki)