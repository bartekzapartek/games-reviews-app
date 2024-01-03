import mysql.connector
import json

# --------------------------------------------------------------

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

# --------------------------------------------------------------

def create_database(mycursor):
    mycursor.execute(f'CREATE DATABASE IF NOT EXISTS {DATABASE_NAME};')
  
def use_database(mycursor):
    mycursor.execute(f'USE {DATABASE_NAME}')

def create_tables(mycursor):
    try:
        mycursor.execute(f'CREATE TABLE {USER_TABLE_NAME} (user_id INT PRIMARY KEY AUTO_INCREMENT, username VARCHAR(50), email VARCHAR(100),password_hash VARCHAR(255), created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);')

        mycursor.execute(f'CREATE TABLE {GAMES_TABLE_NAME} (game_id INT PRIMARY KEY AUTO_INCREMENT,title VARCHAR(100),developer VARCHAR(100), release_date DATE, genre VARCHAR(50));')

        mycursor.execute(f'CREATE TABLE {REVIEWS_TABLE_NAME} (review_id INT PRIMARY KEY AUTO_INCREMENT,user_id INT,game_id INT,rating INT CHECK (rating >= 1 AND rating <= 5),review_text TEXT,review_date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,FOREIGN KEY (user_id) REFERENCES Users(user_id),FOREIGN KEY (game_id) REFERENCES Games(game_id));')
    
    except:
        print("[WARNING] Tabels already created.")


# --------------------------------------------------------------

def get_data():
    file_name = 'database/games.json'
    with open(file_name, 'r') as file: data = json.load(file)

    games = [(entry['title'], entry['developer'], entry['release_date'], entry['genre']) for entry in data]
    return games

def fill_games_table(database):
    mycursor = database.cursor()

    mycursor.execute('SELECT title FROM Games;')
    
    if len(mycursor.fetchall()) != 0: return

    games = get_data()

    mycursor.executemany(f'INSERT INTO {GAMES_TABLE_NAME} (title, developer, release_date, genre) VALUES (%s, %s, %s, %s)', games)
    
    database.commit()


# --------------------------------------------------------------


def init():

    database, mycursor = connect_database()

    create_database(mycursor)
    use_database(mycursor)

    create_tables(mycursor)
    
    fill_games_table(database)

    database.close()



   





    