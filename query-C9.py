import cx_Oracle
import shutil
import os

#User Inputs
filePath = raw_input("Enter File Path of Container List...")
print '/n'
outputDirectory = raw_input("Enter Output Directory...")

#Create an array of part numbers
with open(filePath) as f:
    containerList = f.read().splitlines()

#Create a new instance connection with credentials
#Get db user inputs
dbuser = raw_input("Enter Oracle User")
dbpass = raw_input("Enter password")
dbip = raw_input("Enter Oracle database IP")
dbport = raw_input("Enter Port")
dbSID = raw_input("Enter SID")
dsn_tns = cx_Oracle.makedsn(ip, port, SID)

#Connect to database (taken from http://stackoverflow.com/questions/245465/cx-oracle-connecting-to-oracle-db-remotely)
try:
    conn = cx_Oracle.connect(dbuser, dbpass, dsn_tns)
except:
    print "Failed to connect to C9 database"
cur = conn.cursor()

#Iterate though the array and push the results onto the empty array
for container in containerList:
#       Query database by container
#       Find image and save
#       Loop? Through each image associated with container and save?

#Terminate program
