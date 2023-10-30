import mysql.connector
db_base=mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='Reena@345',
    
)

cursorOjb=db_base.cursor()
cursorOjb.execute("CREATE DATABASE employee_track")
print("All Done!")