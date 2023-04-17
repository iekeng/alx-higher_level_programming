#!/usr/bin/python3
import MySQLdb
import sys
"""Displays all values in the states table where name matches the argument"""i


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", passwd=sys.argv[2],
                         user=sys.argv[1], port=3306, db="hbtn_0e_0_usa")
    cursor = db.cursor()

    rows = cursor.execute("SELECT * FROM states WHERE name LIKE BINARY
                          '{}'".format(sys.argv[4]))

    for row in rows:
        print(row)
    cursor.close()
    db.close()
