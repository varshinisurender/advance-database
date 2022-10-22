import sqlite3

connection = sqlite3.connect("pets.db")

cursor = connection.cursor()

rows = cursor.execute("select name, kind from pet, species where pet.species_id = species.id")

print(rows)

rows = list(rows)

for row in rows:
    name, kind = row
    print(name, kind)
    print(f"my {kind} was named {name}.")

cursor.execute("delete from pet where species_id == 3")
connection.commit()

print("updated")
