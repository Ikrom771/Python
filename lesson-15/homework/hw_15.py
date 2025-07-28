import sqlite3
conn = sqlite3.connect('school.db')
cur = conn.cursor() 

cur.execute(''' CREATE TABLE IF NOT EXISTS Roster (
        Name TEXT,
        Species TEXT,
        Age INTEGER
    )
''')

cur.executemany('''
    INSERT INTO Roster (Name, Species, Age)
    VALUES (?, ?, ?)
''', [
    ('Benjamin Sisko', 'Human', 40),
    ('Jadzia Dax', 'Trill', 300),
    ('Kira Nerys', 'Bajoran', 29)
]
)
cur.execute('''
    UPDATE Roster
    SET Name = ?
    WHERE Name = ?
''', ('Ezri Dax', 'Jadzia Dax'))


# Step 4: Display Name and Age where Species is Bajoran
cur.execute('''
    SELECT Name, Age
    FROM Roster
    WHERE Species = 'Bajoran'
''')

results = cur.fetchall()

print("Bajoran Members:")
for row in results:
    print(f"Name: {row[0]}, Age: {row[1]}")

# Finalize
conn.commit()
conn.close()
