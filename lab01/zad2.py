class Adres:
    def __init__(self, ulica, numer_domu, miasto, kod_pocztowy, numer_mieszkania=None):
        self.ulica = ulica
        self.numer_domu = numer_domu
        self.miasto = miasto
        self.kod_pocztowy = kod_pocztowy
        self.numer_mieszkania = numer_mieszkania

    def show(self):
        adres_print = f"{self.ulica} {self.numer_domu}"
        if self.numer_mieszkania is not None:
            adres_print += f"/{self.numer_mieszkania}"
        adres_print += f"\n{self.kod_pocztowy} {self.miasto}"
        print(adres_print)

    def comes_before(self, other):
        return self.kod_pocztowy <= other.kod_pocztowy

adres1 = Adres("ul. Iwaszkiewicza", "18", "Olsztyn", "10-089")
adres2 = Adres("ul. Tuwima", "2", "Piła", "64-920", "3")

adres1.show()
adres2.show()

if adres2.comes_before(adres1):
    print("adres nr1 znajduje się przed adresem nr2 według kodu pocztowego.")
else:
    print("adres2 znajduje się przed adresem1 według kodu pocztowego.")