import sqlite3

conn = sqlite3.connect("gehalt.db")
cursor = conn.cursor()

sql = "CREATE TABLE personen(name TEXT, vorname TEXT, p_num INTEGER PRIMARY KEY, gehalt FLOAT)"

cursor.execute(sql)

sql = "INSERT INTO personen VALUES('Jan','Baier','3455','4300')"
cursor.execute(sql)
sql = "INSERT INTO personen VALUES('Meyer','Ute','3456','2300')"
cursor.execute(sql)

conn.commit()

conn.close()

