from tuote import Tuote
from ostos import Ostos

class Ostoskori:
    def __init__(self):
        self.ostokset = []
        # ostoskori tallettaa Ostos-oliota, yhden per korissa oleva Tuote

    def tavaroita_korissa(self):
        
        maara = 0
        for ostos in self.ostokset:
            maara += ostos.lukumaara()
        return maara 
        # kertoo korissa olevien tavaroiden lukumäärän
        # eli jos koriin lisätty 2 kpl tuotetta "maito", tulee metodin palauttaa 2 
        # samoin jos korissa on 1 kpl tuotetta "maito" ja 1 kpl tuotetta "juusto", tulee metodin palauttaa 2 

    def hinta(self):
        yht = 0
        
        for osto in self.ostokset:
            yht += osto.hinta()
        return yht
        # kertoo korissa olevien ostosten yhteenlasketun hinnan

    def lisaa_tuote(self, lisattava: Tuote):
        for ostos in self.ostokset:
            if ostos.tuote == lisattava:
                ostos.muuta_lukumaaraa(1)
                return
        self.ostokset.append(Ostos(lisattava))

    def poista_tuote(self, poistettava: Tuote):
        for ostos in self.ostokset:
            if ostos.tuote == poistettava:
                ostos.muuta_lukumaaraa(-1)
        

    def tyhjenna(self):
        self.ostokset = []

    def ostoslista(self):
        return self.ostokset
        # palauttaa listan jossa on korissa olevat ostos-oliot
        # kukin ostos-olio siis kertoo mistä tuotteesta on kyse JA kuinka monta kappaletta kyseistä tuotetta korissa on
