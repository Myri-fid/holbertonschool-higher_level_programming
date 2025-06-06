#!/usr/bin/python3
"""This function connects to the MySQL """
import MySQLdb
import sys


def list_cities_by_state():
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
        SELECT cities.name
        FROM cities
        JOIN states ON cities.state_id = states.id
        WHERE states.name = %s
        ORDER BY cities.id ASC
    """
    cursor.execute(query, (sys.argv[4],))
    cities = cursor.fetchall()
    print(", ".join([city[0] for city in cities]))

    cursor.close()
    conn.close()


if __name__ == "__main__":
    list_cities_by_state()
