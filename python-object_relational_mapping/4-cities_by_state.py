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

    query = """
    SELECT cities.id, cities.name, states.name
    FROM cities
    JOIN states ON cities.state_id = states.id
    ORDER BY cities.id ASC
    """

    cursor.execute(query)

    cities = cursor.fetchall()

    for city in cities:
        print(city)

    cursor.close()
    conn.close()


if __name__ == "__main__":
    list_cities()
