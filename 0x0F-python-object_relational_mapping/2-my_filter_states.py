#!/usr/bin/python3
"""Displays all values in the states table where name matches the argument"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", passwd=sys.argv[2],
                         user=sys.argv[1], port=3306, db=sys.argv[3])
    cursor = db.cursor()

    cursor.execute("SELECT * FROM states WHERE name LIKE BINARY'{}'"
                   .format(sys.argv[4]))
    rows = cursor.fetchall()
    for row in rows:
        print(row)

    cursor.close()
    db.close()
