import mysql.connector


def get_db_connection():
    return mysql.connector.connect(
        host='localhost',
        database='cazapp',
        user='admin',
        password='admin'
    )