from kps_pelaaja_vs_pelaaja import KPSPelaajaVsPelaaja
from kps_tekoaly import KPSTekoaly
from kps_parempi_tekoaly import KPSParempiTekoaly

class KPSTehdas:
    def parempi_tekoaly():
        return KPSParempiTekoaly().pelaa()

    def tekoaly():
        return KPSTekoaly().pelaa()

    def pelaaja_vs_pelaaja():
        return KPSPelaajaVsPelaaja().pelaa()