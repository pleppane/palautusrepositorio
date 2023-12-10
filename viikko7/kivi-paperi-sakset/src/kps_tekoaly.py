from kivi_paperi_sakset import KiviPaperiSakset
from tekoaly import Tekoaly

class KPSTekoaly(KiviPaperiSakset):
    def __init__(self):
        self.__tekoaly = Tekoaly()
        
    def _toisen_siirto(self, ensimmaisen_siirto):
        tokan_siirto = self.__tekoaly.anna_siirto()
        print(f"Tietokone valitsi: {tokan_siirto}")
        return tokan_siirto
