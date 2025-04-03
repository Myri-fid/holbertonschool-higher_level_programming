#!/usr/bin/python3
import MySQLdb
import sys

def list_cities_by_state():
    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=sys.argv[1],
        passwd=sys.argv[2],
        db=sys.argv[3],
    )

    cursor = conn.cursor()
    