import mysql.connector

conn = mysql.connector.connect(
    host="localhost", user="root",
    password="Vikashravi@05", database="school"
)
cursor = conn.cursor()

# Create a table
cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INT AUTO_INCREMENT PRIMARY KEY,
        name VARCHAR(100) NOT NULL,
        age INT
    )
""")

# Create (insert)
cursor.execute("INSERT INTO students (name, age) VALUES (%s, %s)", ("Vikash", 22))
conn.commit()

# Read
cursor.execute("SELECT * FROM students")
for row in cursor.fetchall():
    print(row)

# Update
cursor.execute("UPDATE students SET age = %s WHERE name = %s", (23, "Vikash"))
conn.commit()

# Delete
cursor.execute("DELETE FROM students WHERE name = %s", ("Vikash",))
conn.commit()

cursor.close()
conn.close()