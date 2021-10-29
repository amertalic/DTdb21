# Program extracting first column
import openpyxl
# Import letters for columns
from openpyxl.utils import get_column_letter
# import date cleaner and verification function
from utils import date_cleaner
# import function for capitalizing
from utils import capitalize_string, title_string

# accessing excel
wb = openpyxl.load_workbook('excel_unprocessed/2021-5-PETVET-BAZA EXCEL.xlsx')
ws = wb.active

# print value from a specific cell
print(ws['A1'].value)
print(ws['A2'].value)
print(ws['A3'].value)
print(ws['A4'].value)
print(ws['A5'].value)

# prints all sheets in excel file
print(wb.sheetnames)
# TODO print length of sheets
# TODO check which sheet is the correct one

# excel column names_keys
key_excel_list = ['clinic', 'nb_month', 'surgery_date', 'release_date',
                  'vet_name', 'owner_name', 'owner_address', 'dog_name',
                  'advert', 'catcher', 'feeder', 'collarID', 'sex', 'birthdate',
                  'breed', 'coat', 'weight', 'pregnancy',
                  'fetal_number', 'complications', 'rabies_vaccine', 'ear_tag',
                  'microchip', 'picture', 'comments']

# dictionary where keys will be inserted
row_dict = {}


# gets values from extracted excel row and puts them to the correspondent

def extract_row_values():
    # range (5,6): takes the row between = row 5 only!
    for row in range(5, 6):
        for i in range(25):
            row_dict[key_excel_list[i]] = ws[get_column_letter(i + 1) + str(row)].value
    return row_dict


# runs function for extraction of values from a row in excel file
extract_row_values()
# runs function for date cleaning: surgery_date
row_dict['surgery_date'] = date_cleaner(row_dict['surgery_date'])
# runs function for date cleaning: release_date
row_dict['release_date'] = date_cleaner(row_dict['release_date'])

# TEST PRINT
print(row_dict)
print(type(row_dict['surgery_date']))


# capitalize word in a string
for key in ['owner_name','dog_name','catcher','feeder','rabies_vaccine', 'owner_address']:
    if row_dict[key] != None:
        if key == 'owner_address':
            # capitalize only first word
            row_dict[key] = capitalize_string(row_dict[key])
        else:
            # capitalize all words
            row_dict[key] = title_string(row_dict[key])



print(row_dict['owner_address'])
print(row_dict['owner_name'])
print(row_dict['catcher'])

