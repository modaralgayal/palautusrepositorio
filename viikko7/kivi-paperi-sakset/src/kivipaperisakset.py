from tuomari import Tuomari

class KiviPaperiSakset:
    def pelaa(self):
        tuomari = Tuomari()

        ekan_siirto = self._ensimmaisen_siirto()
        tokan_siirto = self._toisen_siirto(ekan_siirto)

        while self._onko_ok_siirto(ekan_siirto) and self._onko_ok_siirto(tokan_siirto):
            first_move = self._ensimmaisen_siirto()
            second_move = self._toisen_siirto()

            if not first_move or not second_move:
                break

            tuomari.kirjaa_siirto(first_move, second_move)

        print("Kiitos!")
        print(tuomari)

    def _ensimmaisen_siirto(self):
        move = input("Ensimmäisen pelaajan siirto: ")
        self.check_first_move(move)
        return move
    
    def check_first_move(self, move):
        pass

    # tämän metodin toteutus vaihtelee eri pelityypeissä
    def _toisen_siirto(self):
        # metodin oletustoteutus
        return input("Toisen pelaajan siirto: ")

    def _onko_ok_siirto(self, siirto):
        return siirto == "k" or siirto == "p" or siirto == "s"
