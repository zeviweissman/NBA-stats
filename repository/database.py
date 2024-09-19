import psycopg2
from psycopg2 import connect, OperationalError
from psycopg2.extras import RealDictCursor
from config.config import POSTGRES_URI, NBA_DB_URI






create_nba_db_query = "CREATE DATABASE nba_db"
drop_nba_db_query = "DROP DATABASE nba_db"
create_players_table_query = """
CREATE TABLE IF NOT EXISTS players (
    player_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    player_id_str VARCHAR(50) NOT NULL,
    player_name VARCHAR(50) NOT NULL,
    position VARCHAR(10) NOT NULL,
    games INTEGER NOT NULL,
    three_percent FLOAT NOT NULL,
    two_percent FLOAT NOT NULL,
    atr FLOAT NOT NULL,
    ppg FLOAT NOT NULL,
    points INTEGER NOT NULL,
    team VARCHAR(3) NOT NULL,
    season INTEGER NOT NULL
);
"""

create_teams_table_query = """
CREATE TABLE IF NOT EXISTS teams (
    team_id INTEGER PRIMARY KEY GENERATED ALWAYS AS IDENTITY,
    team_name VARCHAR(50) NOT NULL,
    sg_player_id INTEGER NOT NULL,
    sf_player_id INTEGER NOT NULL,
    pg_player_id INTEGER NOT NULL,
    pf_player_id INTEGER NOT NULL,
    c_player_id INTEGER NOT NULL,
    FOREIGN KEY (sg_player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (sf_player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (pg_player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (pf_player_id) REFERENCES players(player_id) ON DELETE CASCADE,
    FOREIGN KEY (c_player_id) REFERENCES players(player_id) ON DELETE CASCADE
);
"""



def get_db_connection():
    connection = connect(NBA_DB_URI, cursor_factory=RealDictCursor)
    return connection



def get_from_database(*query):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(*query)
        to_return = cursor.fetchall()
        return to_return

def change_in_data_base(*query):
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(*query)
        to_return = cursor.fetchone()
        return to_return



def create_db():
    try:
        connection = connect(POSTGRES_URI, cursor_factory=RealDictCursor)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(create_nba_db_query)
    except Exception as e:
        print(f"An error occurred while creating the database: {e}")
    finally:
        connection.close()


def drop_db():
    try:
        connection = connect(POSTGRES_URI, cursor_factory=RealDictCursor)
        connection.autocommit = True
        with connection.cursor() as cursor:
            cursor.execute(drop_nba_db_query)
    except Exception as e:
        print(f"An error occurred while droping the database: {e}")
    finally:
        connection.close()


def create_tables():
    with get_db_connection() as connection, connection.cursor() as cursor:
        cursor.execute(create_players_table_query)
        cursor.execute(create_teams_table_query)



def create_db_if_not_exist():
    try:
        with get_db_connection() as connection:
            create_tables()
    except OperationalError:
            create_db()
            create_tables()



create_db_if_not_exist()