 # Goalkeepers grid

This project is designed to calculate the best combinations of two goalkeepers based on every match of every team

### how it works 

The "modify" files (calendar, team, ranking of previous year) are different for every year.
When this files are initialized it must be run big_basic.py to create a scheme that states the most difficult mathes for each team, this file (big_basic.json) must be copied in big.json, after that it can be used as it is or changed as preferred.

Now it is time to run main.py to create the combinations, that will be visible in the output folder, it is also possible, specifying a team, to see the best combinations for the given team.