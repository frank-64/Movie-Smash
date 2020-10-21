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


def get_titles(conn):
    """ gets all titles from the database file provided
        :param conn: connection instance to database
        :return: titles.fetchall(): all the titles returned from the SQL statement
        """
    cursor = conn.cursor()
    titles = cursor.execute("SELECT movieID, title FROM movie_smash_movies")
    return titles.fetchall()


def url_for_titles(titles, conn):
    for title in titles:
        try:
            cursor = conn.cursor()
            sql = "UPDATE movie_smash_movies SET image_url = '{url}' WHERE movieID = '{id}'".format(url='url working',
                                                                                                    id=title[0])
            cursor.execute(sql)
            conn.commit()
        except Exception as d:
            print(d)






def get_url_by_title(title):
    url = ""
    # Query
    google_url = "https://www.google.co.in/search?q=" + query + "&source=lnms&tbm=isch"
    result = requests.get(url)

    # if successful parse the download into a BeautifulSoup object, which allows easy manipulation
    if result.status_code == 200:
        soup = BeautifulSoup(result.content, "html.parser")

    # find img class
    img = soup.find('table', {'class': 'wikitable sortable'})
    return url





def main():
    # Create connection to database file
    conn = create_connection(database)

    # Getting all titles along with their movieID as this will be needed when inserting back into the database
    titles = get_titles(conn)
    url_for_titles(titles, conn)


if __name__ == '__main__':
    main()
