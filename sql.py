import findspark
from pyspark.sql import SparkSession
import pyspark.pandas as ps
import matplotlib.pyplot as plt
findspark.init()
from pyspark.sql import SparkSession
spark = SparkSession.builder.master("local[*]").getOrCreate()
spark

import sqlalchemy
import mysql.connector

df = ps.read_csv("all_seasons.csv") #dataframe for NBA player info

#connection to local sql database
connection = mysql.connector.connect(host="localhost", user='root', password='kobedrop81', database ="NBA2") 

#connection to online database
connection2 = mysql.connector.connect(host="sql5.freesqldatabase.com", user='sql5528226', password='EmTUWrX8H9', database ="sql5528226")

#cursors that connect to database and lets me preform sql operations
cursorObject = connection.cursor()
cursorObject2 = connection2.cursor()

#Creates Database named NBA2
#cursorObject.execute("create database NBA2")



#cursorObject.execute("CREATE TABLE PlayerVsPoints(Player VARCHAR(255), pointsAVG int);")
sql = "INSERT INTO PlayerVsPoints (Player) VALUES (%s)"
val = df["player_name"].head(20)
#cursorObject.executemany(sql,[[name]for name in list(val.to_numpy())])
#connection.commit()
#cursorObject2.execute("CREATE TABLE PlayerVPoints(Player TEXT(255), pointsAVG VARCHAR(255));")
# insert2 = "INSERT INTO PlayerVsPoints (pointsAVG) VALUES (%f)"
# val2 = df["pts"].head(20)
# cursorObject2.executemany(insert2,[[pts]for pts in list(val2.to_numpy())])
# connection2.commit()





o20df = df[ df['pts']> 20] #creates dataframe where it only displays players with more than 20 points scored
playO20 = o20df['player_name'].head(130) #Player name series of players that averaged 20 points or more(first 130)
ptso20 = o20df['pts'].head(130)#Pts series that displays points of players that averaged 20 or more points(first 130)
draftyear = o20df['draft_year'].head(130)#Draft year series of these players
sqlfordb = "INSERT INTO PlayerOver20 (Player) VALUES (%s)"  #Query that inserts player name into Player column
sqlforpts = "INSERT INTO PlayerOver20 (pointsAVG) VALUES (%s)"#Query that inserts points avg into pointsAVG column
sqlfordraft = "INSERT INTO PlayerOver20 (draftYear) VALUES (%s)"#Query that inserts draft year into draftYear Column

#Creates table name PlayerOver20 with coulumns Player, pointsAVG, and draftYear 
#cursorObject.execute("CREATE TABLE PlayerOver20(Player TEXT(255), pointsAVG VARCHAR(255), draftYear VARCHAR(255));")

#executes queries while pulling values from datafame
#cursorObject.executemany(sqlfordb,[[name]for name in list(playO20.to_numpy())])
#cursorObject.executemany(sqlforpts,[[float(pts)]for pts in list(ptso20.to_numpy())])
cursorObject.executemany(sqlfordraft ,[[draft]for draft in list(draftyear.to_numpy())])

#Commit changes to database table
connection.commit()








