import pymysql

conn = pymysql.connect(
    host = "localhost",
    user = "root",
    password = "1234",
    database = "exampledb",
    charset = "utf8mb4",
)

cursor = conn.cursor()

sql = "SELECT * FROM employees"
cursor.execute(sql)
employees = cursor.fetchall()
for employee in employees:
    print(employee)
conn.close()