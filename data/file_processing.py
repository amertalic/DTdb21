import os

directory = os.fsencode("excel_files_folder/excel_unprocessed")

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename in ['__init__.py', '__pycache__']:
        continue
    else:
        print(os.path.join("excel_files_folder/excel_unprocessed", filename))


