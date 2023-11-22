
from .init import connect_database, use_database

def add_user(username, email, password):
    database, cursor = connect_database()

    use_database(cursor)
    
    cursor.execute(f""" 

        INSERT INTO USERS (username, email, password_hash) VALUES ("{username}", "{email}", "{password}");

    """)

    database.commit()
    database.close()


def get_user(username, email = ''):
    database, cursor = connect_database()

    use_database(cursor)

    cursor.execute(f"""

        SELECT username, password_hash FROM Users WHERE username = "{username} OR email = {email}";           

    """)

    user = list(cursor.fetchall())
    database.close()
    return user if len(user) != 0 else None