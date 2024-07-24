import sqlite3

# connect to sqlite3
connection = sqlite3.connect('student.db')

# create a cursor object to insert record,create table, and retrieve data
cursor = connection.cursor()

# create the table
table_info = """
CREATE TABLE Student(
    ID INTEGER PRIMARY KEY,
    Name VARCHAR(25) NOT NULL,
    Class VARCHAR(25),
    Section VARCHAR(25),
    Age INT,
    Marks INT,
    grade VARCHAR(25));
"""
cursor.execute(table_info)

# Insert records in table

cursor.execute('''Insert Into Student values(1,'Priyanshi','IT','A',20,98,'AA')''')
cursor.execute('''Insert Into Student values(2,'Rahul','CS','B',21,95,'AA')''')
cursor.execute('''Insert Into Student values(3,'Riya','IT','A',20,97,'AA')''')
cursor.execute('''Insert Into Student values(4,'Raj','CS','B',21,96,'AA')''')
cursor.execute('''Insert Into Student values(5,'Rohan','IT','A',20,98,'AA')''')
cursor.execute('''Insert Into Student values(6,'Riya','CS','B',21,95,'AA')''')
cursor.execute('''Insert Into Student values(7,'Rajdeep','IT','A',20,97,'AA')''')
cursor.execute('''Insert Into Student values(8, 'Sujal', 'CS', 'B', 21, 96, 'AA')''')

# Displaying records
print('Inserted records are')
data = cursor.execute('Select * from Student')

for row in data:
    print(row)
    
# Close the connection
# Commit your changes in the databse
connection.commit()
connection.close()