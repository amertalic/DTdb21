import os

directory = os.fsencode('C:/Users/AT/Documents/git_projects/DTdb21/data/excel_files_folder/excel_unprocessed')

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(os.path.join(directory, filename))
