import sqlite3

# Connect to the database
conn = sqlite3.connect('it_Department')
cursor = conn.cursor()

# Delete data with category "Testing"
cursor.execute("DELETE FROM HelpDeskTickets WHERE category = 'Testing'")

# Commit the changes
conn.commit()

# Print some debug information
print("Deleted entries with category 'Testing'")

# Close the connection
conn.close()