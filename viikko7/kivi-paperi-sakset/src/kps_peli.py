from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

def luo_peli(tyyppi):
    pelimoodit = {
        "a": KPSPelaajaVsPelaaja,
        "b": KPSTekoaly,
        "c": KPSParempiTekoaly
    }
    if tyyppi not in pelimoodit:
        return None
    return pelimoodit[tyyppi]()
