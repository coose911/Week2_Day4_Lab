import unittest

from src.high_scores import latest, personal_best, personal_top_three,from_highest_to_lowest,top_three_when_there_is_a_tie, top_three_when_there_are_less_than_three,top_three_when_there_are_less_than_one
# Tests adapted from `problem-specifications//canonical-data.json` @ v4.0.0


class HighScoresTest(unittest.TestCase):
    
    # Tests
    def setUp(self):
        self.scores = [100, 0, 90, 30]
        self.scores1 = [30, 30, 25, 100, 0, 40]
        self.scores2 = [20, 4]
        self.scores3 = [40]

    # Test latest score (the last thing in the list)
    def test_latest_score(self):
        self.assertEqual(30, latest(self.scores))
        

    # Test personal best (the highest score in the list)
    def test_personal_best(self):
        self.assertEqual(100, personal_best(self.scores))

    # # Test top three from list of scores
    def test_top_three(self):
        self.assertEqual([100,90,30], personal_top_three(self.scores))

    # Test ordered from highest tp lowest
    def test_from_highest_to_lowest(self):
        self.assertEqual([100,90,30,0], from_highest_to_lowest(self.scores))

    # # Test top three when there is a tie
    def test_top_three_when_there_is_a_tie(self):
        self.assertEqual([100,40,30], top_three_when_there_is_a_tie(self.scores1))

    # # Test top three when there are less than three
    def test_top_three_when_there_are_less_than_three(self):
        self.assertEqual([20, 4], top_three_when_there_are_less_than_three(self.scores2))

    # # Test top three when there is only one
    def test_top_three_when_there_is_one(self):
        self.assertEqual([40], top_three_when_there_are_less_than_one(self.scores3))
    
