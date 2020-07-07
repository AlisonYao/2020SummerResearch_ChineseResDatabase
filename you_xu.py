import openpyxl

#open the workbook
wb = openpyxl.load_workbook('NARA NY CECF DB check list 2020 Summer.xlsx')
#open the sheet
sheet = wb['CHINESE']
#get all entry date infor into a list
def clean_entry_date(sheet):
    lst = []
    for row in range(1, sheet.max_row):
        lst.append(sheet.cell(row, openpyxl.utils.column_index_from_string('AO')).value)
    for i in range(len(lst)):
        value = lst[i]
        if type(value) == type('1'):
            if len(value) == 8:
                year = value[-4:]
                
    return lst

print(clean_entry_date(sheet))