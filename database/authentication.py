import mysql.connector

from init import connect_database

def add_user(username, email, password):
    database, cursor = connect_database()

    cursor.execute(f""" 

        INSERT INTO USERS (username, email, password_hash) VALUES ("{username}", "{email}", "{password}");

    """)

    database.commit()