from kps_tehdas import KPSTehdas


def main():
    while True:
        print("Valitse pelataanko"
              "\n (a) Ihmistä vastaan"
              "\n (b) Tekoälyä vastaan"
              "\n (c) Parannettua tekoälyä vastaan"
              "\nMuilla valinnoilla lopetetaan"
              )
        vastaus = input()

        if any(x in vastaus for x in ("a", "b", "c")):
            print(
                    "Peli loppuu kun pelaaja antaa virheellisen siirron eli jonkun muun kuin k, p tai s"
                )
            if vastaus.endswith("a"):
                KPSTehdas.pelaaja_vs_pelaaja()
            elif vastaus.endswith("b"):
                KPSTehdas.tekoaly()
            elif vastaus.endswith("c"):
                KPSTehdas.parempi_tekoaly()
            else:
                break


if __name__ == "__main__":
    main()
