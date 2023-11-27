import unittest
from unittest.mock import Mock, ANY
from kauppa import Kauppa
from viitegeneraattori import Viitegeneraattori
from varasto import Varasto
from tuote import Tuote

class TestKauppa(unittest.TestCase):
    def test_ostoksen_paaytyttya_pankin_metodia_tilisiirto_kutsutaan(self):
        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock.uusi.return_value = 42

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 10
            elif tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 5)
            if tuote_id == 3:
                return Tuote(3, "juustoa", 5)

        # otetaan toteutukset käyttöön
        varasto_mock.saldo.side_effect = varasto_saldo
        varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

        # alustetaan kauppa
        kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

        # tehdään ostokset
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("pekka", "12345")

        # varmistetaan, että metodia tilisiirto on kutsuttu
        pankki_mock.tilisiirto.assert_called()
        # toistaiseksi ei välitetä kutsuun liittyvistä argumenteista

        
        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(2)
        kauppa.tilimaksu("Pekka Mikkola", "1234-12345")

        pankki_mock.tilisiirto.assert_called()

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(1)
        kauppa.tilimaksu("Pekka Mikkola", "1234-12345")

        pankki_mock.tilisiirto.assert_called()

        kauppa.aloita_asiointi()
        kauppa.lisaa_koriin(1)
        kauppa.lisaa_koriin(3)
        kauppa.tilimaksu("Pekka Mikkola", "1234-12345")

        pankki_mock.tilisiirto.assert_called_with("Pekka Mikkola", viitegeneraattori_mock.uusi(), "1234-12345", "33333-44455", 5)

    def test_aloita_asiointi_metodia_kutsutaan(self):

        pankki_mock = Mock()
        viitegeneraattori_mock = Mock()

        # palautetaan aina arvo 42
        viitegeneraattori_mock = Mock()

        varasto_mock = Mock()

        # tehdään toteutus saldo-metodille
        def varasto_saldo(tuote_id):
            if tuote_id == 1:
                return 10
            elif tuote_id == 2:
                return 10
            elif tuote_id == 3:
                return 0

        # tehdään toteutus hae_tuote-metodille
        def varasto_hae_tuote(tuote_id):
            if tuote_id == 1:
                return Tuote(1, "maito", 5)
            if tuote_id == 2:
                return Tuote(2, "leipä", 5)
            if tuote_id == 3:
                return Tuote(3, "juustoa", 5)

            # otetaan toteutukset käyttöön
            varasto_mock.saldo.side_effect = varasto_saldo
            varasto_mock.hae_tuote.side_effect = varasto_hae_tuote

            # alustetaan kauppa
            kauppa = Kauppa(varasto_mock, pankki_mock, viitegeneraattori_mock)

            # tehdään ostokset
            kauppa.aloita_asiointi()
            kauppa.lisaa_koriin(1)
            kauppa.tilimaksu("pekka", "12345")

            pankki_mock.tilisiirto.assert_called()

            kauppa.aloita_asiointi()
            assert(len(kauppa._ostoskori._tuotteet) == 0)
            viitegeneraattori_mock.uusi.assert_called_once()

    def test_poista_korista(self):
        # Create a mock for varasto and ostoskori
        varasto_mock = Mock()
        ostoskori_mock = Mock()

        # Initialize Kauppa with the mock objects
        kauppa = Kauppa(varasto=varasto_mock)

        # Set the Kauppa's _ostoskori attribute to the mock object
        kauppa._ostoskori = ostoskori_mock

        # Define a tuote mock object
        tuote_mock = Mock()

        # Mock the hae_tuote method to return the tuote mock object
        varasto_mock.hae_tuote.return_value = tuote_mock

        # Call the poista_korista method
        kauppa.poista_korista(1)  # Assuming 1 is the product ID

        # Assert that the expected methods were called
        varasto_mock.hae_tuote.assert_called_once_with(1)
        ostoskori_mock.poista.assert_called_once_with(tuote_mock)
        varasto_mock.palauta_varastoon.assert_called_once_with(tuote_mock)
