import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    passwd='user12345'
)

cursor_object = database.cursor()

cursor_object.execute('CREATE DATABASE crm_crud_db')

print('create db done')