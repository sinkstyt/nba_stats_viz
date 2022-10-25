# NBA player data, including advanced statistics, seasons 1996-2021
* Thanks to Kaggle page for nicely arranged source dataset:
[https://www.kaggle.com/datasets/justinas/nba-players-data/](https://www.kaggle.com/datasets/justinas/nba-players-data/)

### Authors
* Ekene Emenanjor [https://github.com/EkeneE123](https://github.com/EkeneE123)
* Sohum Patel [https://github.com/Sohum7](https://github.com/Sohum7)
* Tyler Sinks [https://github.com/sinkstyt](https://github.com/sinkstyt)

## A quick look at visual answers to questions like:
1. Which team is drafting the most players?
2. Could net rating be used as a predictor for Championship Wins / Dynasties?
3. Who's individual net rating bizarrely varies outside of his cohorts'?
4. Who are the five most mediocre players by season? by career?
5. Find any repeats on the middle 5 -->
>> * consider how to catch the WRONG SUM call to accidently compare across full dataset
6. Consider how to render graphs / visualizations via Tablueau Public
7. Does player height strongly correlate with act%?
8. Which team by decade showed the widest variations in pace?
9. Are there instances of player net rating varying widely from team's?
10. How is hockey's +/- similar to NBA's net rating?

### Dashboard Example
![Rookie Year Assists Averages](https://github.com/sinkstyt/nba_stats_viz/blob/main/Dashboard%201.png?raw=true)

### Some Sample SQL Queries
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

### Problems with the data? Cleaning reccommended?
1. cleaning required?
2. table creation
3. vizualizations, plots, graphs

## License
GPL 2.0+

## Contact
* Ekene Emenanjor [https://github.com/EkeneE123](https://github.com/EkeneE123)
* Sohum Patel [https://github.com/Sohum7](https://github.com/Sohum7)
* Tyler Sinks [https://github.com/sinkstyt](https://github.com/sinkstyt)