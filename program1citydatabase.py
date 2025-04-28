import sqlite3

# Create or connect to the cities database
connection = sqlite3.connect('cities.db')
cursor = connection.cursor()

# Create Cities table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS Cities (
        CityName TEXT,
        Population INTEGER
    )
''')

# Insert 20 cities and their populations
cities_data = [
    ('Tokyo', 37400068),
    ('Delhi', 29399141),
    ('Shanghai', 26317104),
    ('São Paulo', 21846507),
    ('Mumbai', 19980000),
    ('Cairo', 20000000),
    ('Beijing', 20035455),
    ('Dhaka', 19577973),
    ('Mexico City', 21671908),
    ('Osaka', 19222665),
    ('New York City', 18713220),
    ('Karachi', 16093786),
    ('Buenos Aires', 15400000),
    ('Istanbul', 15462452),
    ('Kolkata', 14900000),
    ('Manila', 13482000),
    ('Lagos', 13400000),
    ('Rio de Janeiro', 13452000),
    ('Bangkok', 10400000),
    ('Moscow', 12163131)
]

cursor.executemany('INSERT INTO Cities (CityName, Population) VALUES (?, ?)', cities_data)

# Save changes and close connection
connection.commit()
connection.close()

print("Cities database ready with 20 rows.")
