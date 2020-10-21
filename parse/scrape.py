import requests
from bs4 import BeautifulSoup
import sqlite3

database = 'C:/Users/Frankie/PycharmProjects/Django-Website/db.sqlite3'

def create_connection(db_file):
    """ create a database connection to the SQLite database
        specified by the db_file
    :param db_file: database file
    :return: Connection object or None
    """
    conn = None
    try:
        conn = sqlite3.connect(db_file)
    except Exception as e:
        print(e)

    return conn


def get_titles(cursor):
    titles = cursor.execute("SELECT movieID, title FROM movie_smash_movies")
    return titles.fetchall()


def main():
    # Create connection to database file
    conn = create_connection(database)
    cursor = conn.cursor()

    # Getting all titles along with their movieID as this will be needed when inserting back into the database
    titles = get_titles(cursor)

if __name__ == '__main__':
    main()
