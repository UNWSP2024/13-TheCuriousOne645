import sqlite3

# Connect to the cities database
connection = sqlite3.connect('cities.db')
cursor = connection.cursor()

# Retrieve all rows from the Cities table
cursor.execute('SELECT * FROM Cities')
rows = cursor.fetchall()

# Display the data
print("CityName | Population")
print("---------------------")
for row in rows:
    print(f"{row[0]} | {row[1]}")

connection.close()
