from getScore import Score

class TennisGame:
    def __init__(self, player_1, player_2):
        self.player_1 = player_1
        self.player_2 = player_2
        self.m_score1 = 0
        self.m_score2 = 0

    def won_point(self, player):
        if player == self.player_1:
            self.m_score1 += 1
        elif player == self.player_2:
            self.m_score2 += 1
        else:
            print("Invalid Player")
            return

    def get_score(self):
        score = Score.get_score(self.m_score1, self.m_score2)
        return score