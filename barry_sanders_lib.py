"""
Problem
"""
import csv

def read_csv_into_dict(filename):
    my_dict = {}
    with open(filename, 'r') as infile:
        reader = csv.reader(infile)
        next(reader)
        for row in reader:
            year = int(row[0])
            age = row[1]
            team = row[2]
            games = row[3]
            rushes = row[4]
            rush_yards = row[5]
            rush_tds = row[6]
            targets = row[7]
            receptions = row[8]
            rec_yards = row[9]
            rec_tds = row[10]

            row_data = ( row[0], row[1], row[2], row[4], row[4], row[5], row[6], row[7], row[8], row[9], row[10])

            my_dict[year] = row_data
    return my_dict

def tally_the_stats(row):
    """
    Takes in a list of data (row) and then uses the following
    formula to generate a score for the row:
    * +1 for every game played
    * +5 for every yard rushing
    * +75 for every rushing TD
    * +2 for every reception
    * +10 for every yard receiving
    * +75 for every receiving TD

    calculate the score for the row
    return the total score for the row
    """
    return 0

def find_best_season(list_of_season_score_values):
    """
    take in a list
    This list is a list of tuples ordered pairs (year, score)
    iterate thru the list and find the season that had the best
    total score.
    return the year of that season
    """
    return 1998

def spew_season(player_name, row):
    """
    Takes in a list of a player's season.
    Then print out the stats of the row in a "nice"
    format.
    """
    print(f'{player_name}')



