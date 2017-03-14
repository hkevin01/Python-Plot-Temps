#!/usr/bin/python
import MySQLdb

#-------------------------------------------
db = MySQLdb.connect(host="", # your host, usually localhost
                     user="", # your username
                      passwd="", # your password
                      db="") # name of the data base

# you must create a Cursor object. It will let
#  you execute all the queries you need
cur = db.cursor() 

# Use all the SQL you like
cur.execute("SELECT * FROM moped_prod.Observation where observationTime >= %d AND observationTime <= %d ORDER BY observationTime desc")
#SELECT id,platformId, latitude, longitude ,qualityFlags,observationTime FROM moped_prod.Observation WHERE observationTime >='".$startTime."' AND observationTime<='".$endTime."' ORDER BY observationTime desc";
#-------------------------------------------------
# this line is tricky, try to get it exactly right
#print "If I add %d, %d, and %d I get %d." % (
#    my_age, my_height, my_weight, my_age + my_height + my_weight)


# print all the first cell of all the rows
for row in cur.fetchall() :
    print row[0]
