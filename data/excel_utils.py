# after everything is extracted from excel the file is renamed
# and moved to the folder where all processed excel fiels are.


import shutil


# moves and renames Excel file when processed
shutil.move('excel_files_folder/excel_unprocessed/2021-5-PETVET-BAZA EXCEL.xlsx',
            'excel_files_folder/excel_processed_renamed/' + 'test.xlsx')






