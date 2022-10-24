README.md Group Project

# NBA player data, including advanced statistics, seasons 1996-2021
* Thanks to Kaggle page for nicely arranged source dataset:
[https://www.kaggle.com/datasets/justinas/nba-players-data/](https://www.kaggle.com/datasets/justinas/nba-players-data/)

### Authors
* Ekene Emenanjor [https://github.com/EkeneE123](https://github.com/EkeneE123)
* Sohum Patel [https://github.com/Sohum7](https://github.com/Sohum7)
* Tyler Sinks [https://github.com/sinkstyt](https://github.com/sinkstyt)

# A quick look at visual answers to questions like:
1. Could net rating be used as a predictor for Championship Wins / Dynasties?
2. Who's individual net rating bazarrely varies outside of his cohorts'?
3. Five most mediocre players in this season stretch
* finding any repeats on the middle 5 --> consider how to catch the WRONG
* * SUM call to accidently compare across full dataset
4. 
5. 

### Some Sample Queries (SQL)
1. SELECT `everything`

```
SELECT *
FROM players;
```
2. SELECT all players by name, index by 1) name, 2) team '_abbreviation'
and
ORDER by timeline ('season')
```
SELECT DISTINCT player_name,
FROM players
GROUP BY player_name, team_abbreviation
ORDER BY season;
```

3. Sort by total career points
```
SQL code <HERE>


```

4. Sort by total career points AND
compare against any changes in pace throughout season?
```

SQL snippet here

```

5. Consider how to render graphs / visualizations via Tablueau Public
* including:
>> Does net rating lead to championships?
>> Height against act% -- what IS act%
>> 5 medians from every unique catagetory... "like looking for the most mediocre of the NBA year by year
>> >> any repeats in the mediocres?

## License
GPL 2.0+


## Contact


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

# # Problems with the data? Cleaning reccommended?
1. cleaning required?
2. table creation
3. vizualizations, plots, graphs
