import urllib
import urllib.request
from selenium import webdriver
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
            sql = "UPDATE movie_smash_movies SET image_url = '{url}' WHERE movieID = '{id}'".format(url=get_url_by_title(title[1]),
                                                                                                    id=title[0])
            cursor.execute(sql)
            conn.commit()
        except Exception as d:
            print(d)

def get_url_by_title(title):
    url = "https://www.google.co.in/search?q=" + title + "&source=lnms&tbm=isch"
    browser = webdriver.Chrome('chromedriver.exe')
    browser.get(url)
    header = {
        'User-Agent': "Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/43.0.2357.134 Safari/537.36"}

    for _ in range(500):
        browser.execute_script("window.scrollBy(0,10000)")

    for x in browser.find_elements_by_xpath('//img[contains(@class,"rg_i Q4LuWd")]'):
        source = x.get_attribute('src')
        try:
            if('https' in source):
                print("Title: {title} Source: {s}".format(title=title, s=source))
                return source
        except:
            None
    browser.close()


def main():
    # Create connection to database file
    conn = create_connection(database)

    # Getting all titles along with their movieID as this will be needed when inserting back into the database
    titles = get_titles(conn)
    url_for_titles(titles, conn)



if __name__ == '__main__':
    main()