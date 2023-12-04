from tennisgame import TennisGame


def main():
    
    game_play = TennisGame("player1","player2",0,0)
    game_play.point_won("player1")
    game_play.point_won("player1")
    game_play.point_won("player2")
    game_play.point_won("player1")
    game_play.point_won("player1")


if __name__=="__main__":
    main()