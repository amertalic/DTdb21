import os
import pandas as pd


def get_excel_file_paths(path_exception_folder):
    directory = os.path.join(path_exception_folder, 'data','excel_files_folder', 'excel_unprocessed')
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
    return unprocessed_files


print(get_excel_file_paths(''))
# rename file and move it to the processed folder
