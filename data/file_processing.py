import os
import pandas as pd

directory = os.fsencode("excel_files_folder/excel_unprocessed")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename in ['__init__.py', '__pycache__']:
        continue
    else:
        print(os.path.join(os.getcwd(),"excel_files_folder/excel_unprocessed", filename))
        excel = pd.read_excel(os.path.join(os.getcwd(), "excel_files_folder/excel_unprocessed", filename))

        print(excel)




