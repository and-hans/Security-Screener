import sqlite3

database = sqlite3.connect("analysis.db")

cursor = database.cursor()

# cursor.execute("""CREATE TABLE Security (
#    Ticker TEXT,
#    price REAL,
#    SharesOwned INTEGER,
#    Worth REAL
# )""")

# cursor.commit()

cursor.close()
