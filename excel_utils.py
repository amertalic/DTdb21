# after everything is extracted from excel the file is renamed
# and moved to the folder where all processed excel files are.


import shutil


def move_rename_xlsx(new_name):
    # moves and renames Excel file when processed
    shutil.move('data/excel_files_folder/excel_unprocessed/2021-5-PETVET-BAZA EXCEL.xlsx',
                'excel_files_folder/excel_processed_renamed/' + new_name + 'xlsx')
