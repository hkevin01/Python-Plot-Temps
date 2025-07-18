#!/usr/bin/python
"""
connect.py

Connects to a MySQL database and fetches data.
"""

import MySQLdb


def main():
    """Main function to connect to MySQL and fetch data."""
    db = MySQLdb.connect(host="localhost", user="root", passwd="password", db="mydb")
    cur = db.cursor()
    cur.execute("SELECT * FROM mytable")
    for row in cur.fetchall():
        print(row[0])
    db.close()


if __name__ == "__main__":
    main()
