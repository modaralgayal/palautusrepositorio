from tuomari import Tuomari
from tekoaly import Tekoaly


class KPSTekoaly:
    def __init__(self):
        self.tekoaly = Tekoaly()

    def check_second_move(self):
        move = self.tekoaly.anna_siirto()
        print("AI move", move)
        return move