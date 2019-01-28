## Imported the data file into a list

import csv
f = open("nfl_suspensions_data.csv", "U")
nfl_suspensions = csv.reader(f)
nfl_suspensions = list(nfl_suspensions)

## Remove the header row

nfl_suspensions = nfl_suspensions[1:len(nfl_suspensions)]

## Number of domestic violence occurences per year.

years = {}
for row in nfl_suspensions:
    row_year = row[5]
    
    if row_year in years:
        years[row_year] = years[row_year] + 1
    else:
        years[row_year] = 1
        
print(years)


## Analyzing by the data by the teams and games column

teams = [row[1] for row in nfl_suspensions]
unique_teams = set(teams)

games = [row[2] for row in nfl_suspensions]
unique_games = set(games)

print(unique_teams)
print(unique_games)

## Created a Suspension class to represent each suspension and to convert the year from a string to integer

class Suspension():
    def __init__(self, row):
        self.name = row[0]
        self.team = row[1]
        self.games = row[2]
        
        try:
            self.year = int(row[5])
        except Exception:
            self.year = 0
    
    def get_year(self): 
        return(self.year)
        
third_suspension = Suspension(nfl_suspensions[2])

missing_year = Suspension(nfl_suspensions[22])
twenty_third_year = missing_year.get_year()






