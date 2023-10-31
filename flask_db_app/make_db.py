import sqlite3

conn = sqlite3.connect('it_Department')
                     
# Create a cursor object to interact with the database
cursor = conn.cursor()

# Create a table to store your data (example table)
cursor.execute('''CREATE TABLE IF NOT EXISTS HelpDeskTickets (
                   infoID INTEGER PRIMARY KEY,
                   question TEXT,
                   response TEXT,
                   responseDate DATE,
                   category VARCHAR(255))''')

for row in cursor:
    print('row = %r' % (row,))

# Commit the changes and close the connection
conn.commit()
conn.close()