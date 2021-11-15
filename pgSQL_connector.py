import psycopg2
from excel_extractor import extract_row_values

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
    # print("from pgSQL_connector", row_dict)
    cursor.execute(
        f"insert into dogs (clinic, nb_month, surgery_date,"
        f"release_date, vet_name, owner_name, owner_address, "
        f"dog_name, advert, catcher, feeder, collarid, sex, "
        f"breed, coat, weight, pregnancy, fetal_number,"
        f"complications, rabies_vaccine, ear_tag, microchip, picture, comments, age, excel_name) "
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

# commit the transaction
connection.commit()
# close the connection
connection.close()
