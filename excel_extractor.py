# Program extracting first column
import openpyxl
# Import letters for columns
from openpyxl.utils import get_column_letter

wb = openpyxl.load_workbook('excel_files/2021-5-PETVET-BAZA EXCEL.xlsx')
ws = wb.active

# print value from a specific cell
print(ws['A5'].value)

# prints all sheets in excel file
print(wb.sheetnames)

# excel column names_keys
key_excel_list = ['clinic', 'nb_month', 'surgery_date', 'release_date',
                  'vet_name', 'owner_name', 'owner_address', 'dog_name',
                  'advert', 'catcher', 'feeder', 'collarID', 'sex', 'birthdate',
                  'breed', 'coat', 'weight', 'pregnancy',
                  'fetal_number', 'complications', 'rabies_vaccine', 'ear_tag',
                  'microchip', 'picture', 'comments']

# dictionary where keys will be inserted
row_dict = {
    'clinic': '',
    'nb_month': '',
    'surgery_date': '',
    'release_date': '',
    'vet_name': '',
    'owner_name': '',
    'owner_address': '',
    'dog_name': '',
    'advert': '',
    'catcher': '',
    'feeder': '',
    'collarID': '',
    'sex': '',
    'birthdate': '',
    'breed': '',
    'coat': '',
    'weight': '',
    'pregnancy': '',
    'fetal_number': '',
    'complications': '',
    'rabies_vaccine': '',
    'ear_tag': '',
    'microchip': '',
    'picture': '',
    'comments': ''
}
def extract_row_values():
    for row in range(5, 6):
        for i in range(25):
            row_dict[key_excel_list[i]] = ws[get_column_letter(i+1) + str(row)].value
    return row_dict

