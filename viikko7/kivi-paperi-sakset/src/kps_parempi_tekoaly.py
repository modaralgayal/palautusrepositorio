from tuomari import Tuomari
from tekoaly_parannettu import TekoalyParannettu


class KPSParempiTekoaly:
    def __init__(self):
        self.tekoaly = TekoalyParannettu(10)

    def check_first_move(self, move):
        self.tekoaly.aseta_siirto(move)
