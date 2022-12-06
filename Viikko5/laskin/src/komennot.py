

class Summa:
    def __init__(self, sovellus, lukija):
        self.sovellus = sovellus
        self.lukija = lukija

    def suorita(self):
        return self.sovellus.plus(int(self.lukija()))


class Erotus:
    def __init__(self,  sovellus, lukija):
        self.sovellus = sovellus
        self.lukija = lukija

    def suorita(self):
        return self.sovellus.miinus(int(self.lukija()))


class Nollaus:
    def __init__(self,  sovellus, lukija):
        self.sovellus = sovellus
        self.lukija = lukija

    def suorita(self):
        return self.sovellus.nollaa()


class Kumoa:
    def __init__(self,  sovellus, lukija):
        self.sovellus = sovellus
        self.lukija = lukija

    def suorita(self):
        return self.sovellus.kumoa()
