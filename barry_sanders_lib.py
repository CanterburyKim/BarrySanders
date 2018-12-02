"""
Problem
"""
import csv

def read_csv_into_dict(filename):
    """
    Take in the filename and read the data
    from it (csv) and populate a dictionary
    with the key being the year and the
    value being a TUPLE containing all the individual
    values of each row (basically the full row as
    a tuple)
    """
    my_dict = {}

    # TODO: read and populate the dictionary
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
