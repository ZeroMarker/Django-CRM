import mysql.connector

dataBase = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='password',
)

# Prepare cursor object
cursorObject = dataBase.cursor()

# Create database
cursorObject.execute("CREATE DATABASE ROMA;")

print("All done!")

# Create superuser
# python mange.py createsuperuser
