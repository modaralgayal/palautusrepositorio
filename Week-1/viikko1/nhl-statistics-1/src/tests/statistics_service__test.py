import unittest
from statistics_service import StatisticsService
from player import Player



class PlayerReaderStub:
    def get_players(self):

        return [
            Player("Semenko", "EDM", 4, 12),
            Player("Lemieux", "PIT", 45, 54),
            Player("Kurri",   "EDM", 37, 53),
            Player("Yzerman", "DET", 42, 56),
            Player("Gretzky", "EDM", 35, 89)
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
    
    def test_top(self): 
        top_players = self.stats.top(3) 

        expected_names = ["Gretzky", "Lemieux", "Yzerman"]
        actual_names = [player.name for player in top_players]
        self.assertEqual(actual_names, expected_names)