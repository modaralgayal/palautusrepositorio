class Player:
    def __init__(self, player_dict):
        self.name = player_dict.get('name', '')
        self.nationality = player_dict.get('nationality', '')
        self.assists = player_dict.get('assists', 0)
        self.goals = player_dict.get('goals', 0)
        self.penalties = player_dict.get('penalties', 0)
        self.team = player_dict.get('team', '')
        self.games = player_dict.get('games', 0)

    def __str__(self):
        return f"{self.name.ljust(20)} {self.team.ljust(4)} {str(self.goals).rjust(2)} + {str(self.assists).rjust(2)} = {str(self.goals + self.assists).rjust(3)}"

