#!/usr/bin/python3
"""lists all states starting with the letter 'N' in the db"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", port=3306, passwd=sys.argv[2],
                         user=sys.argv[1], db=sys.argv[3])
    cursor = db.cursor()
    cursor.execute("SELEct * FROM states WHERE name LIKE
                   BINARY 'N%' ORDER BY states.id")
    rows = cursor.fetchall()
    for row in rows:
        print(row)
    cursor.close()
    db.close()
