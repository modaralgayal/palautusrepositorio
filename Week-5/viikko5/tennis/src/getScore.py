class Score:
    def get_score(m_score1, m_score2):

        score = ""
        temp_score = 0

        if m_score1 == m_score2:
            if m_score1 == 0:
                score = "Love-All"
            elif m_score1 == 1:
                score = "Fifteen-All"
            elif m_score1 == 2:
                score = "Thirty-All"
            elif m_score1 == 3:
                score = "Forty-All"
            else:
                score = "Deuce"
        elif m_score1 >= 4 or m_score2 >= 4:
            minus_result = m_score1 -  m_score2

            if minus_result == 1:
                score = "Advantage player1"
            elif minus_result == -1:
                score = "Advantage player2"
            elif minus_result >= 2:
                score = "Win for player1"
            else:
                score = "Win for player2"
        else:
            for i in range(1, 3):
                if i == 1:
                    temp_score = m_score1
                else:
                    score = score + "-"
                    temp_score = m_score2

                if temp_score == 0:
                    score = score + "Love"
                elif temp_score == 1:
                    score = score + "Fifteen"
                elif temp_score == 2:
                    score = score + "Thirty"
                elif temp_score == 3:
                    score = score + "Forty"
        return score
