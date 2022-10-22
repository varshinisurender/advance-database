import sqlite3

#DB-API

connection = sqlite3.connect("pets.db")

cursor = connection.cursor()

try:
    cursor.execute("drop table pet")
except:
    pass

try:
    cursor.execute("drop table species")
except:
    pass

cursor.execute("create table pet(id integer primary key, name text, species_id int)")

cursor.execute("create table species(id integer primary key, kind text)")

cursor.execute("insert into species (kind) values ('dog')")
cursor.execute("insert into species (kind) values ('cat')")
cursor.execute("insert into species (kind) values ('fish')")

cursor.execute("insert into pet (name,species_id) values ('puppy',1)")
cursor.execute("insert into pet (name,species_id) values ('micky',2)")
cursor.execute("insert into pet (name,species_id) values ('suzy',1)")
cursor.execute("insert into pet (name,species_id) values ('angel',3)")

connection.commit()
connection.close()

print("done")


