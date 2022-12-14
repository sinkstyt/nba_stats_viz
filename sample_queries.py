# df.keys()
# //
# # # '_c0', 'player_name', 'team_abbreviation', 'age', 'player_height',
#           'player_weight', 'college', 'country', 'draft_year', 'draft_round',
#           'draft_number', 'gp', 'pts', 'reb', 'ast', 'net_rating', 'oreb_pct',
#           'dreb_pct', 'usg_pct', 'ts_pct', 'ast_pct', 'season'],
#        dtype='object'

# A few endpoint visualizations brought over from the README (or not):

# A quick setup to make sure modules are installed:
# 
# !pip install pyspark
# !pip install findspark
# !pip install mysql-connector-python
# 
# 
# 
# Consdier these questions for selection and sort of data --> visual answers:


# 1. Could net rating be used as a predictor for Championship Wins / Dynasties?
import findspark
# findspark.init()
from pyspark.sql import SparkSession
import pyspark.pandas as ps
import matplotlib.pyplot as plt
import pandas as pd
%matplotlib inline
ps.set_option('compute.ops_on_diff_frames', True)


# 2. Who's individual net rating bazarrely varies outside of his cohorts'?
# 3. Five most mediocre players in this season stretch
# * finding any repeats on the middle 5 --> consider how to catch the WRONG
# * * SUM call to accidently compare across full dataset
# 4. 
# 5. 

### Some Sample Queries (SQL)
```
SELECT *
FROM players;

// Sort by total career points

// Sort by total career points and compare against any changes in pace throughout season?

// 

# Are we going to put the whole database in one table?
# Yes, for now
# <!-- 1. I think we can show each of the relationships we're hoping to show via dashboard in Tableau Public
# * including:
# >> Does net rating lead to championships?
# >> Height against act% -- what IS act%
# >> 5 medians from every unique catagetory... "like looking for the
# >> >> mediocre-IST of the NBA - year to year"
# >>
# >>
# >>
# 2. What about the documentation?
# * git commits not required?
# * shared repo
# *   -->


-- with sums by player_name across as many seasons as are available



-- any trends along timeline of a career for net rating?


-- sort for distinct names



-- -- possibility for different spelling year-on-year?

-- Most points (heighest 25, highest 5)

-- Most net rating change over career
top 25, top 5

-- Broad logic questions used to write queries for data selection


From MySQL scratchfile:


SELECT player_name, points
FROM people;

SELECT *
FROM people;

SELECT *
FROM people
LIMIT 25;

SELECT *
FROM people
LIMIT 5;


1. points over the course / career
-- SQL query in order to make an inset table for points scrutiny

SELECT "player_name, points (by season)"