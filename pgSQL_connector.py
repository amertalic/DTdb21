import psycopg2

# connect to the db
connection = psycopg2.connect(
    host = "localhost",
    database = "DTbih",
    user = "postgres",
    password = "4545"
)

# cursor
cursor = connection.cursor()
cursor.execute("insert into dogs (owner_name, dog_name, microchip) values ('Amer', 'Belly', 023456789112345)")
# enter data into table
#cursor.execute("insert into Clinics (name) values ('Veterinarska stanica Ketti')")

# execute query
cursor.execute("select * from dogs")
rows = cursor.fetchall()

for r in rows:
    print(r, type(r))

# commit the transaction
connection.commit()
# close the connection
connection.close()
