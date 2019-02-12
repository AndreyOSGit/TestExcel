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
cshki = ''
CforTasks = sheet.col_values(cell_number_with_C)
print(CforTasks)
taskN = [int(k) for k in sheet.col_values(cell_check)]
taskNset = list(set(taskN))
print(taskN)
print(taskNset)
listCover = []
for i in range(0, CforTasks.__len__()):
        for j in range(0, taskNset.__len__()):
            for p in range(0, CforTasks.__len__()):
                if taskN[p] == taskNset[j]:
                    cshki = cshki + ', ' + CforTasks[p]
                # print(cshki)
                # print(CforTasks)
            listCover.append(cshki)
            cshki = ''
print(listCover)
a = list(set(listCover))
out = []
print('a')
print(a)
# sheet.cell(i, cell_number_with_C).value)
for i in range(0,col_with_c_len-1):
    for x in a:
        if (x.__contains__ (CforTasks[i])):
            out.append('Покрыть проверки: ' + x)
print('out')
print(out)
# for i in range(1,col_with_c_len):
#     sheet.update_cell(i, cell_new, out[i])