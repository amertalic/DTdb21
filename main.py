import os

# import pandas as pd

# loop through excel files in the unprocessed folder
# excel file list
directory = os.path.join('data', 'excel_files_folder', 'excel_unprocessed')
unprocessed_files = []
for file in os.listdir(directory):
    filename = os.fsdecode(file)
    if filename in ['__init__.py', '__pycache__']:
        continue
    else:
        file_path = os.path.join(os.getcwd(), str(directory), filename)
        unprocessed_files.append(file_path)
        # try:
        #     excel = pd.read_excel(os.path.join(os.getcwd(), "excel_files_folder/excel_unprocessed", filename))
        # except:
        #     continue

# get the first file from the unprocessed folder

# process the first file

# import into postgres row by row

# rename the first file

# move the first file
