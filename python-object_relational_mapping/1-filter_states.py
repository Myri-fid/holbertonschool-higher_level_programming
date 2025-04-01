#!/usr/bin/python3
import MySQLdb
import sys
"""This function connects to the MySQL """



def list_states():
    """This function connects to the MySQL """

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = conn.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC")

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    conn.close()

if __name__ == "__main__":
    list_states()
