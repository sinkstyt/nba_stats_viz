README.md Group Project

# NBA player data, including advanced statistics, seasons 1996-2021
* Thanks to Kaggle page for nicely arranged source dataset:
[https://www.kaggle.com/datasets/justinas/nba-players-data/](https://www.kaggle.com/datasets/justinas/nba-players-data/)

### Authors
* Ekene Emenanjor
* Sohum Patel
* Tyler Sinks

# A quick look at visual answers to questions like:
1. Could net rating be used as a predictor for Championship Wins / Dynasties?
2. Who's individual net rating bazarrely varies outside of his cohorts'?
3. Five most mediocre players in this season stretch
* finding any repeats on the middle 5 --> consider how to catch the WRONG
* * SUM call to accidently compare across full dataset
4. 
5. 

### Some Sample Queries (SQL)
```
SELECT *
FROM players;

// Sort by total career points

// Sort by total career points and compare against any changes in pace throughout season?

// 

# Are we going to put the whole database in one table?
# Yes, for now
<!-- 1. I think we can show each of the relationships we're hoping to show via dashboard in Tableau Public
* including:
>> Does net rating lead to championships?
>> Height against act% -- what IS act%
>> 5 medians from every unique catagetory... "like looking for the
>> >> mediocre-IST of the NBA - year to year"
>>
>>
>>
2. What about the documentation?
* git commits not required?
* shared repo
*   -->

## License
GPL 2.0+


## Contact


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


>> return *only* the top 25 . Consider checks for outlier years.

--> filter reassigned to select top 5



>> capture the median 25 players for medi*ocrity* across entire career

>> Anyway, besides designing a NEW statistic, talk about controlling for pace
>> across season --> which team by decade showed the widest variations IN PACE?

2. net rating predicts championships?

3. net rating individual varying widely against own team's

4. How is hockey's +/- different from NBA's net rating?

5. 

# # Problems with the data:
1. cleaning required?
2. table creation
3. vizualizations, plots, graphs
4. 
