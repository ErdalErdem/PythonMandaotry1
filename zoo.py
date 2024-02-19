import sqlite3

conn = sqlite3.connect(':memory:')
cursor = conn.cursor()

cursor.execute('''CREATE TABLE Animal
               (id INTEGER PRIMARY KEY, 
                name TEXT, 
                species TEXT, 
                age INTEGER)''')

animals = [('Elephant', 'Mammal', 10),
           ('Tiger', 'Mammal', 5),
           ('Parrot', 'Bird', 2)]
cursor.executemany('INSERT INTO Animal (name, species, age) VALUES (?, ?, ?)', animals)

conn.commit()

# Read from the database and print the animals
cursor.execute('SELECT * FROM Animal')
animals = cursor.fetchall()

conn.close()

print(animals)
