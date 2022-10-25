# NBA Players’ Statistics Glossary and Discussion

### all column names for statistics from all_seasons.csv dataset:
* ‘gp' --> games played
* 'pts' --> points
* 'reb' --> rebounds (offensive and defensive)
* 'ast' --> assists (count)

### then some of the advanced statistics, not so intuitive:
* 'net_rating',
* 'oreb_pct',
* 'dreb_pct',
* 'usg_pct',
* 'ts_pct',
* 'ast_pct'

## net rating =
* calculated at the team level.
* Net rating comes from subtracting a team’s defensive rating from same team’s offensive rating. How is offensive rating calculated?
* net rating **does account for pace** —> the statistic controls for the variations due to different possession counts per game
* for NBA statistics, net rating considers point differential of team per 100 possessions
* net rating correlates positively with point differential
* A net rating of 0 means that a team is exactly average in terms of point differential.
* A higher net rating means the team is outscoring its opponents; negative: underscoring opponents
* can be used to track a team’s performance over time AND compare two teams’ net ratings to arrive at a decent, meaningful comparison of those two teams’ game by game performance
* **notable exception** to this trend in recent playoff play: Miami Heat (2014) won championship while carrying a -0.8 net rating
* Golden State Warriors over past five seasons have maintained >10 net rating. Over this 5-year span, achieved a +10.1 net rating —> an NBA record
* does **not account for:** strength of schedule or injuries
* at the player level, net rating acts sort of like hockey’s +/- statistic: when the player is on the court for that teams’ most recent 100 possessions, player’s team outscored opponents(+) or no(-)?

## oreb pct =
* offensive rebound percentage
* The percentage of available offensive rebounds a player obtains (actually rebounds) while on the floor. Can also be measured at team level.

## dreb pct =
* defensive rebound percentage
* formula is:
```
            *  successful defensive rebounds
            * ———————————————
            * defensive rebounds + other team’s offensive rebounds
```
* sort of saying that of all the possible rebounds available at a particular basket throughout the game, the team/player grabbed what percent of all these opportunities.
* 'Dreb pct', only considers those rebound opportunities while defending

## usg_pct =
* “usage percentage”
##### from basketball-reference.com:
* Usage Percentage has been available since the 1977-78 season in the NBA
* has the formula:
```
    100 * ((FGA + 0.44 * FTA + TOV) * (Tm MP / 5))
    -----------------------------------------------
      (MP * (Tm FGA + 0.44 Tm FTA + Tm TOV))
```
* Usage percentage is an estimate of the percentage of team plays used by a player while he was on the floor.

## ts pct =
* “true shooting percentage”
* a measure of scoring efficiency based on the number of points scored over the number of possessions in which they attempted to score
* a more nuanced statistic than the simpler Field Goal Percentage, which is:
>> * field goals made divided by all field goal attemts
>> * FG% does a poor job accounting for the difficulty of shots (doesn’t control for 3-pt shots versus free throws, etc.)
* “effective fieldgoal percentage” or eFG% is another step closer towards “ts” from plain old FG%
>> * eFG% multiplies by 0.5 made three-point shots and adds that to numerator (thus: FGM + 0.5 3PM)
>> * eFG%, then, is an effective measure of shooting percentage but completely ignores the free throw (“the most valuable shot in basketball”)
>> * to more closely get at the points per shooting possession — including getting fouled during shooting and then making 77.1% of free throws… — we need additional adjustment that even eFG% does not accomplish
* 0.44 is the best approximate sweet-spot coefficient intended to consider all the possibilities (technical fouls, and-ones, free throws after a missed 3-pointer, etc…)
* formula:
```
                   Points 
    ----------------------——————————————————
  FieldGoal Attempts + 0.44 * FreeThrowAttempts
```
* actual TS% formula moves the statistic into a percent scale by multiplying the whole denominator by 2

## ast pct =
* assists percentage
* The percentage of teammate field goals a player assisted on while they were on the floor
* assists completed by player out of all the assist completed by player’s team while the player is on the court
* formula:
```
                         100 * Assists
      -----------------------------—————————————————————————
( Minutes Played / (Team Minutes/5) ) * Team Field Goals Made – Field Goals Made
```
### NBA STATS explains it as:
* The percentage of teammate field goals a player assisted on while they were on the floor
* Formula - by player:
```
                  Assists by this player
        -------------——————————————————————————
    ( Team’s FieldGoals Made - FieldGoals Made by Player )
```