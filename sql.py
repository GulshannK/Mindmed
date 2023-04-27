import sqlite3



conn = sqlite3.connect('Sessionslist.db')

cursor = conn.cursor()

# cursor.execute('''CREATE TABLE Member (Member_id INTEGER PRIMARY KEY NOT NULL, First_name VARCHAR(255) NOT NULL, Last_name VARCHAR(255) NOT NULL, SocialSecurity INTEGER NOT NULL, Email VARCHAR(255) NOT NULL, address VARCHAR(255) NOT NULL, Comments VARCHAR(255)NOT NULL )''')
# cursor.execute('''CREATE TABLE Employee (Member_id INTEGER PRIMARY KEY NOT NULL, First_name VARCHAR(255) NOT NULL, Last_name VARCHAR(255) NOT NULL, SocialSecurity INTEGER NOT NULL, Email VARCHAR(255) NOT NULL, address VARCHAR(255) NOT NULL, Comments VARCHAR(255)NOT NULL )''')

# cursor.execute("INSERT INTO Member (id, First_name,Last_name, SocialSecurity, Email, address, Comments) VALUES (?, ?, ?, ?, ? , ? , ?)", (1, 'Hannah', 'Clark','100001-0111', 'hannah.clark@gmail.com', '909 First St', NULL))
# cursor.execute("INSERT INTO Member (id, First_name,Last_name, SocialSecurity, Email, address, Comments) VALUES (?, ?, ?, ?, ? , ? , ?)", (2, 'joe', 'hamer','100001-0122', 'hannah.clark@gmail.com', '909 First St', NULL))
# cursor.execute("INSERT INTO Member (id, First_name,Last_name, SocialSecurity, Email, address, Comments) VALUES (?, ?, ?, ?, ? , ? , ?)", (3, 'Isam', 'Hamo','100001-0133', 'hannah.clark@gmail.com', '909 First St', NULL))
# cursor.execute("INSERT INTO Member (id, First_name,Last_name, SocialSecurity, Email, address, Comments) VALUES (?, ?, ?, ?, ? , ? , ?)", (4, 'kavish', 'Solanki','100001-0144', 'hannah.clark@gmail.com', '909 First St', NULL))
# cursor.execute("INSERT INTO Member (id, First_name,Last_name, SocialSecurity, Email, address, Comments) VALUES (?, ?, ?, ?, ? , ? , ?)", (5, 'josh', 'De Seiana','100001-0155', 'hannah.clark@gmail.com', '909 First St', NULL))
# cursor.execute("INSERT INTO Member (id, First_name,Last_name, SocialSecurity, Email, address, Comments) VALUES (?, ?, ?, ?, ? , ? , ?)", (6, 'Gulshan', 'Kumar','100001-0166', 'hannah.clark@gmail.com', '909 First St', NULL))
# cursor.execute("INSERT INTO Employee (id, First_name,Last_name, SocialSecurity, Email, address, Comments) VALUES (?, ?, ?, ?, ? , ? , ?)", (6, 'hamo', 'isam','100001-0177', 'hannah.clark@gmail.com', '909 First St', NULL))

cursor.execute("SELECT * FROM Member")
rows = cursor.fetchall()

for row in rows:
    print(row)

# conn.commit()

conn.close()
