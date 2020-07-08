import openpyxl
import 

#open the workbook
wb = openpyxl.load_workbook('NARA NY CECF DB check list 2020 Summer.xlsx')
#open the sheet
sheet = wb['CHINESE']

def get_col_number(sheet, name):
    for col in range(1, sheet.max_column + 1):
        if sheet.cell(1, col).value == name:
            return col
    
#get all entry date infor into a list
def clean_entry_date(sheet):
    lst = []
    col = get_col_number(sheet, 'ENTRYDATE')
    for row in range(2, sheet.max_row + 1):
        lst.append(sheet.cell(row, col).value)

    years = []
    months = []
    days = []
    for i in range(len(lst)):
        value = lst[i]
        if type(value) == type('1'):
            if len(value) == 8:
                year = value[-4:]
                month = value[0:2]
                if value[2:4] == '  ':
                    day = None
                else:
                    day = value[2:4]
            elif len(value) == 4:
                year = value
                month = None
                day = None
        else:
            year = None
            month = None
            day = None
        years.append(year)
        months.append(month)
        days.append(day)

    return lst

print(clean_entry_date(sheet)[0])