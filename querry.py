import sqlite3

conn = sqlite3.connect("leads.db")
cursor = conn.cursor()

cursor.execute("SELECT * FROM leads;")
print(cursor.fetchall())  # <-- Check if leads exist in the database

conn.close()
