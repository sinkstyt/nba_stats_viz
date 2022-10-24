import pyspark.pandas as ps
import matplotlib.pyplot as plt
import pyarrow
import findspark
findspark.init()
from pyspark.sql import SparkSession
import mysql.connector
from mysql.connector import errorcode

spark = SparkSession.builder.master("local[*]").getOrCreate()
sparkContext = spark.sparkContext

df = ps.read_csv("all_seasons.csv")
df.describe()

#df.plot(kind='scatter', x='player_name', y='player_height')
#df.plot(kind='scatter', x='player_weight', y='player_height')
#df.plot(kind='scatter', x='age', y='draft_round')
#df.plot(kind='scatter', x='player_height', y='pts')

# player_name dataframe
player_names_s = df['player_name'].unique()
#print(player_names_s)

player_names_df2 = player_names_s.to_frame()
#print(player_names_df2)

type(player_names_s)
#type(player_names_df2)


def useNbaPlayerStatsDB(cursor, conn):
    sql_ex = "CREATE DATABASE IF NOT EXISTS nba_player_stats;"
    cursor.execute(sql_ex)
    sql_ex = "USE nba_player_stats;"
    cursor.execute(sql_ex)

    conn.commit()

def addPlayerNamesTable(df, cursor, conn, commit=True):
    player_names_s = df['player_name'].unique()

    sql_ex = "CREATE TABLE IF NOT EXISTS player_names (player_name VARCHAR(255) PRIMARY KEY);"
    cursor.execute(sql_ex)

    if commit:
        conn.commit()

    sql_ex = "INSERT IGNORE INTO player_names (player_name) VALUES (%s);"
    # print( type([ (name, )  for name in (player_names_df.to_list()) ]) )
    # res = sql_cursor.executemany(sql_ex, [ (name, )  for name in player_names_df.to_list() ])
    cursor.executemany(sql_ex, [(name,) for name in list(player_names_s.to_numpy())])

    if commit:
        conn.commit()

def addPlayerPhysAttrsTable(df, cursor, conn, commit=True):
    sql_ex = "CREATE TABLE IF NOT EXISTS player_phys_attrs (" \
             "player_name  VARCHAR(255)          ," \
             "age          INT           NOT NULL," \
             "height       FLOAT(20)     NOT NULL," \
             "weight       FLOAT(20)     NOT NULL," \
             "FOREIGN KEY (player_name) REFERENCES player_names(player_name)" \
             ");"
    cursor.execute(sql_ex)

    if commit:
        conn.commit()

    sql_ex = "INSERT IGNORE INTO player_phys_attrs (player_name, age, height, weight) " \
             "VALUES (%s, %s, %s, %s);"

    #pa_df = df[['player_name', 'age', 'player_height', 'player_weight']]
    playername = [str(pn) for pn in df['player_name'].to_list()]
    age = [int(age) for age in df['age'].to_list()]
    height = [float(ph) for ph in df['player_height'].to_list()]
    weight = [float(pw) for pw in df['player_weight'].to_list()]
    tuples = list(zip(playername, age, height, weight))

    #pa_df_records = pa_df.to_records()
    #pa_df_tuples = [list(rec)[1:] for rec in pa_df_records]

    cursor.executemany(sql_ex, tuples)

    if commit:
        conn.commit()

def addPlayerProfAttrsTable(df, cursor, conn, commit=True):
    sql_ex = "CREATE TABLE IF NOT EXISTS player_prof_attrs (" \
             "player_name  VARCHAR(255)         ," \
             "gp          INT           NOT NULL," \
             "pts         FLOAT(20)     NOT NULL," \
             "reb         FLOAT(20)     NOT NULL," \
             "ast         FLOAT(20)     NOT NULL," \
             "net_rating  FLOAT(20)     NOT NULL," \
             "oreb_pct    FLOAT(20)     NOT NULL," \
             "dreb_pct    FLOAT(20)     NOT NULL," \
             "usg_pct     FLOAT(20)     NOT NULL," \
             "ts_pct      FLOAT(20)     NOT NULL," \
             "ast_pct     FLOAT(20)     NOT NULL," \
             "season      VARCHAR(8)    NOT NULL," \
             "FOREIGN KEY (player_name) REFERENCES player_names(player_name)" \
             ");"
    cursor.execute(sql_ex)

    if commit:
        conn.commit()

    sql_ex = "INSERT INTO player_prof_attrs (player_name, gp, pts, reb, ast, net_rating, oreb_pct, dreb_pct, usg_pct, ts_pct, ast_pct, season) " \
             "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s);"

    player_name = [str(pn) for pn in df['player_name'].to_list()]
    gp = [int(gp) for gp in df['gp'].to_list()]
    pts = [float(pts) for pts in df['pts'].to_list()]
    reb = [float(reb) for reb in df['reb'].to_list()]
    ast = [float(ast) for ast in df['ast'].to_list()]
    net_rating = [float(net_rating) for net_rating in df['net_rating'].to_list()]
    oreb_pct = [float(oreb_pct) for oreb_pct in df['oreb_pct'].to_list()]
    dreb_pct = [float(dreb_pct) for dreb_pct in df['dreb_pct'].to_list()]
    usg_pct = [float(usg_pct) for usg_pct in df['usg_pct'].to_list()]
    ts_pct = [float(ts_pct) for ts_pct in df['ts_pct'].to_list()]
    ast_pct = [float(ast_pct) for ast_pct in df['ast_pct'].to_list()]
    season = [str(season) for season in df['season'].to_list()]

    tuples = list(zip(player_name, gp, pts, reb, ast, net_rating, oreb_pct, dreb_pct, usg_pct, ts_pct, ast_pct, season))

    cursor.executemany(sql_ex, tuples)

    if commit:
        conn.commit()




pass



sql = None
need_database = True
if not need_database:
    exit(1)

try:
    host = "localhost"
    user = "root"
    psswrd = ""
    sql = mysql.connector.connect(host=host, user=user, password=psswrd)
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print("Something is wrong with your user name or password")
    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print("Database does not exist")
    else:
        #print(err)
        pass
except:
    print("ERROR")

if sql is None:
    exit(1)

sql_cursor = sql.cursor()

try:
    # Sets up database with name 'nba_player_stats' if one does not exist
    useNbaPlayerStatsDB(sql_cursor, sql)  # Required

    # Creates a table with name 'player_names' if one does not exist and populates
    addPlayerNamesTable(df, sql_cursor, sql, True)  # Optional

    # Creates a table with name 'player_phys_attrs' if one does not exist and populates
    addPlayerPhysAttrsTable(df, sql_cursor, sql, True)  # Optional

    # Creates a table with name 'player_prof_attrs' if one does not exist and populates
    addPlayerProfAttrsTable(df, sql_cursor, sql, True)  # Optional
except Exception as e:
    print(f"ERROR:{e}")

sql_cursor.close()
sql.close()
