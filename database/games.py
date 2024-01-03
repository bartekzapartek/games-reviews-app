from .init import connect_database, use_database
from .init import GAMES_TABLE_NAME

def get_games_titles(limit = 0):
    database, cursor = connect_database()
    use_database(cursor)

    cursor.execute(f"SELECT title FROM {GAMES_TABLE_NAME}")

    games = list(cursor.fetchall())
    games = [x[0] for x in games]
    database.close()

    return games if len(games) != 0 else None

def get_game(id):
    database, cursor = connect_database()

    cursor.execute(f"SELECT * FROM {GAMES_TABLE_NAME} WHERE game_id = id")

    games = list(cursor.fetchall())
    database.close()

    return games if len(games) != 0 else None