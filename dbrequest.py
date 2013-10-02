import sqlite3

conn = sqlite3.connect("gehalt.db")
cursor = conn.cursor()

sql = "SELECT * FROM personen"
cursor.execute(sql)

for d in cursor:
	print d
	for person in d:
		print person
	
conn.close()