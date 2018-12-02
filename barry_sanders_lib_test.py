"""
Test cases for list lib
"""
from barry_sanders_lib import *
import unittest
import os

my_dir = os.path.dirname(os.path.realpath(__file__))
filename = 'barry_sanders_stats.csv'
my_dict = read_csv_into_dict(my_dir + '/' + filename)
# print(my_dict)


class TestBarry(unittest.TestCase):
    def test_most_rush_yards(self):
        year_with_most_rush_yards = find_year_with_most_rush_yards(my_dict)
        best_year = my_dict[year_with_most_rush_yards]
        spew_season('Barry Sanders', best_year)
        assertEqual(best_year, 1997)

    def test_most_rush_tds(self):
        year_with_most_rush_tds = find_year_with_most_rush_tds(my_dict)
        best_year = my_dict[year_with_most_rush_tds]
        spew_season('Barry Sanders', best_year)
        assertEqual(best_year, 1991)

    def test_general(self):
        list_of_season_scores = []
        for key in my_dict:
            row = my_dict[key]
            score = tally_the_stats(row)
            year_score_tuple = (key,score)
            list_of_season_scores.append( year_score_tuple )

        print (list_of_season_scores)

        year_of_best_season = find_best_season(list_of_season_scores)
        best_season_row = my_dict[year_of_best_season]

        spew_season('Barry Sanders', best_season_row)
        assertEquals(year_of_best_season, 1997)



if __name__ == '__main__':
    unittest.main()
