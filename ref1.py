import sqlite3
db = sqlite3.connect('something.db')
cursor = db.cursor()
sql = "SELECT * FROM Colour;"
cursor.execute(sql)
results = cursor.fetchall()
# print nicely
for colour in results:
    print(f"Colour: {colour[1]}\nHex code: {colour[2]}\n")

# close the db
db.close()

