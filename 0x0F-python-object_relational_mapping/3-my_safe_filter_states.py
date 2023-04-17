#!/usr/bin/python3
"""lists all states from the db"""
import sys
import MySQLdb


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cursor = db.cursor()
    name = sys.argv[4]
    cursor.execute("""SELECT * FROM states WHERE name = %s""", (name,))

    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
