import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="Vikashravi@05",
    database="school"
)

print("Connected!" if conn.is_connected() else "Failed")
conn.close()