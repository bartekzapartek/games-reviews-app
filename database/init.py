import mysql.connector

HOST = 'localhost'
USER = 'root'
PASSWD = 'bartekzapartek'
PORT = '3306'

DATABASE_NAME = 'games_review'

USER_TABLE_NAME = 'Users'
GAMES_TABLE_NAME = 'Games'
REVIEWS_TABLE_NAME = 'Reviews'


def connect_database():

    database = mysql.connector.connect(

        host = HOST,
        user = USER,
        passwd = PASSWD,
        port = PORT

    )

    mycursor = database.cursor()
    return database, mycursor


def create_database(mycursor):
    mycursor.execute(f'CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};')
  
def use_database(mycursor):
    mycursor.execute(f'USE {DATABASE_NAME}')

def create_tables(mycursor):
    try:
        mycursor.execute(f'CREATE TABLE {USER_TABLE_NAME} (user_id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), email VARCHAR(100),password_hash VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')

        mycursor.execute(f'CREATE TABLE {GAMES_TABLE_NAME} (game_id INT PRIMARY KEY AUTO_INCREMENT,title VARCHAR(100),developer VARCHAR(100),publisher VARCHAR(100),release_date DATE,genre VARCHAR(50));')

        mycursor.execute(f'CREATE TABLE {REVIEWS_TABLE_NAME} (review_id INT PRIMARY KEY AUTO_INCREMENT,user_id INT,game_id INT,rating INT CHECK (rating >= 1 AND rating <= 5),review_text TEXT,review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (user_id) REFERENCES Users(user_id),FOREIGN KEY (game_id) REFERENCES Games(game_id));')
    
    except:
        print("[WARNING] Tabels already created.")

        # INSERT INTO USERS (username, email, password_hash) VALUES ("krzys", "krzys@mail.com", "bartek123");
        # INSERT INTO USERS (username, email, password_hash) VALUES ("janek", "janek@mail.com", "bartek123");
        # INSERT INTO USERS (username, email, password_hash) VALUES ("martyna", "martyna@mail.com", "bartek123");
        # INSERT INTO USERS (username, email, password_hash) VALUES ("piotrek", "piotrek@mail.com", "bartek123");

def fill_tables(database):
    mycursor = database.cursor()

    mycursor.execute(""" 

        INSERT INTO USERS (username, email, password_hash) VALUES ("bartek", "bartek@mail.com", "bartek123");

    """)

    database.commit()


def init():

    database, mycursor = connect_database()

    create_database(mycursor)
    use_database(mycursor)

    create_tables(mycursor)

    database.close()



   





    