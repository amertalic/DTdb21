import psycopg2
from excel_extractor import extract_row_values
from datetime import datetime
# move and rename files
import shutil

# connect to the db
connection = psycopg2.connect(
    host="localhost",
    database="DTbih",
    user="postgres",
    password="4545"
)




# cursor
cursor = connection.cursor()
# loops through all rows in the excel
for row_number in range(9):

    row_dict = extract_row_values(row_number)

    # crete new file name for the excel file to be renamed after processing
    # new  file_name = clinic name + first surgery date + date and time of the time of processing
    # so that name is unique
    if row_number == 0:
        surgery_date = str(row_dict['surgery_date'])
        surgery_date = surgery_date.replace('-', '') + '_'
        clinic = row_dict['clinic'].replace(' ','') + '_'
        file_name = clinic + surgery_date + str(datetime.now().strftime("%Y%m%d_%H%M%S"))
    # print("from pgSQL_connector", row_dict)

    cursor.execute(
        f"insert into dogs (clinic, nb_month, surgery_date, release_date, vet_name, owner_name, owner_address, dog_name, advert, catcher, feeder, collarid, sex, breed, coat, weight, pregnancy, fetal_number, complications, rabies_vaccine, ear_tag, microchip, picture, comments, age, excel_name) "
        f"values ("
        f"'{row_dict['clinic']}', '{row_dict['nb_month']}', '{row_dict['surgery_date']}', "
        f"'{row_dict['release_date']}', '{row_dict['vet_name']}', '{row_dict['owner_name']}', "
        f"'{row_dict['owner_address']}', '{row_dict['dog_name']}', '{row_dict['advert']}', "
        f"'{row_dict['catcher']}', '{row_dict['feeder']}', '{row_dict['collarID']}', "
        f"'{row_dict['sex']}', '{row_dict['breed']}', "
        f"'{row_dict['coat']}', '{row_dict['weight']}', '{row_dict['pregnancy']}', "
        f"'{row_dict['fetal_number']}', '{row_dict['complications']}', '{row_dict['rabies_vaccine']}', "
        f"'{row_dict['ear_tag']}', '{row_dict['microchip']}', '{row_dict['picture']}', "
        f"'{row_dict['comments']}', '{row_dict['age']}', '{row_dict['excel_name']}')")
    print(row_dict['excel_name'])
# execute query
cursor.execute("select * from dogs")
rows = cursor.fetchall()

for r in rows:
    print(r, type(r))

# after a all data from the xlsx file is imported into postgres
# the file will be renamed into vet clinic + surgery_date + today's date
# and moved renamed to the processed folder
# to the postgres dogs table a new column will be added referencing the renamed excel file from wich the data was retrived


# import function to move and rename excel file when finished importing
# after everything is extracted from excel the file is renamed
# and moved to the folder where all processed excel files are.

# moves and renames Excel file when processed
shutil.move('data/excel_files_folder/excel_unprocessed/2021-5-PETVET-BAZA EXCEL.xlsx',
            'data/excel_files_folder/excel_processed_renamed/' + file_name + '.xlsx')

# commit the transaction
connection.commit()
# close the connection
connection.close()
