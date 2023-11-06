import unittest
from statistics_service import StatisticsService
from player import Player
from enum import Enum



class SortBy(Enum):
    POINTS = 1
    GOALS = 2 
    ASSISTS = 3


class PlayerReaderStub:
    def get_players(self):
        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54), # 99
            Player("Kurri",   "EDM", 37, 53), # 90
            Player("Yzerman", "DET", 42, 56), # 98
            Player("Gretzky", "EDM", 35, 89)  # 124
        ]
    


class TestStatisticsService(unittest.TestCase):
    def setUp(self):

        self.stats = StatisticsService(
            PlayerReaderStub()
        )
    
    def test_initiation(self):

        first_player = self.stats._players[0]
        player_stats = f"{first_player.name} {first_player.team} {first_player.goals} + {first_player.assists} = {first_player.points}"
        self.assertEqual(player_stats ,"Semenko EDM 4 + 12 = 16")
    
    def test_search(self):
        
        self.assertEqual(self.stats.search("Bellingham"),None)
        self.assertEqual(self.stats.search("Yzerman").name,"Yzerman")
    
    def test_team(self):
        players_in_team = self.stats.team("EDM")
        self.assertTrue(players_in_team[0].name == "Semenko")
        self.assertTrue(players_in_team[1].name == "Kurri")
        self.assertTrue(players_in_team[2].name == "Gretzky")
    
    def test_top_points(self):
        top_players = self.stats.top(3, SortBy.POINTS)
        expected_names = ["Gretzky", "Lemieux", "Yzerman"]
        actual_names = [player.name for player in top_players]
        self.assertEqual(actual_names, expected_names)

    def test_top_goals(self):
        top_players = self.stats.top(3, SortBy.GOALS)
        expected_names = ["Lemieux", "Yzerman", "Kurri"]

        for name in expected_names:
            self.assertIn(name, [player.name for player in top_players])


    def test_top_assists(self):
        top_players = self.stats.top(3, SortBy.ASSISTS)
        expected_names = ["Gretzky", "Yzerman", "Lemieux"]

        for name in expected_names:
            self.assertIn(name, [player.name for player in top_players])

