#!/usr/bin/python3
"""list all the cities of a state"""
import sys
import MySQLdb

if __name__ == '__main__':
    db = MySQLdb.connect(host='localhost', user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3],
                         port=3306)
    cursor = db.cursor()
    state_name = sys.argv[4]
    cursor.execute("""SELECT cities.name
                   FROM cities
                   INNER JOIN states
                   ON states.id = cities.state_id
                   WHERE state.name = %s""", (state_name,))

    rows = cursor.fetchall()
    tmp = list(row[0] for row in rows)
    print(*tmp, sep=', ')

    cursor.close()
    db.close()
