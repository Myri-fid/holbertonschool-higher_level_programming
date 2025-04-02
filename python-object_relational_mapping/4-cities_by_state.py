#!/usr/bin/python3
"""This function connects to the MySQL """
import MySQLdb
import sys


def list_cities():
    """This function connects to the MySQL """

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = conn.cursor()

    query = "SELECT * FROM cities WHERE BINARY name = '{}'" \
        "ORDER BY id ASC".format(sys.argv[4])
    cursor.execute(query)

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    list_cities()
