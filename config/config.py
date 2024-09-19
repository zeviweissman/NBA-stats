import os

POSTGRES_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost/postgres')
NBA_DB_URI = os.getenv('DATABASE_URL', 'postgresql://postgres:1234@localhost/nba_db')