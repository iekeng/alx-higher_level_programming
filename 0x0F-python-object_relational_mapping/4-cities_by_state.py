#!/usr/bin/python3
"""list cities and states"""
import sys
import MySQLdb

if __name__ == 'main':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELECT cities.id, states.name, cities.name
                   FROM cities
                   INNER JOIN states
                   ON states.id=cities.state_id")

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
