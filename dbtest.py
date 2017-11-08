import sqlite3
conn = sqlite3.connect('example.db')
c = conn.cursor()

# Create table

#c.execute("INSERT INTO user VALUES (NULL, 'yyecust','姚远','信息工程','2015')")

# Save (commit) the changes
#conn.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
#conn.close()
for row in c.execute("SELECT * FROM user WHERE name='姚远'"):
    print(row)