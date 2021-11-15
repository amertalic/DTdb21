import os

directory = os.fsencode('excel_unprocessed')

for file in os.listdir(directory):
    filename = os.fsdecode(file)
    print(os.path.join(directory, filename))
