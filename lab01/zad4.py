class Car:
    def __init__(self, wydajnosc_paliwa, maks_pojemnosc):
        self.wydajnosc_paliwa = wydajnosc_paliwa  #wydajność paliwowa w km/litr
        self.maks_pojemnosc = maks_pojemnosc  #maksymalna pojemność baku w litrach
        self.poziom_paliwa = 0  #początkowy poziom paliwa

    def drive(self, dystans):
        potrzebne_paliwo = dystans / self.wydajnosc_paliwa

        if potrzebne_paliwo <= self.poziom_paliwa:
            self.poziom_paliwa -= potrzebne_paliwo
            print(f"Przebyto dystans: {dystans} km. Aktualny poziom paliwa: {self.poziom_paliwa} litrów")
        else:
            print("Brak wystarczającej ilości paliwa.")

    def get_fuel_level(self):
        return self.poziom_paliwa

    def add_fuel(self, ilosc_paliwa_dodanego):
        #przy tankowaniu nie można przekroczyć maksymalnej pojemności baku
        if self.poziom_paliwa + ilosc_paliwa_dodanego <= self.maks_pojemnosc:
            self.poziom_paliwa += ilosc_paliwa_dodanego
            print(f"Zatankowano {ilosc_paliwa_dodanego} litrów. Aktualny poziom paliwa: {self.poziom_paliwa} litrów")
        else:
            print("Nie można zatankować więcej paliwa, bo przekroczono pojemność baku.")

my_car = Car(10, 50)  #obiekt klasy Car z wydajnościa paliwowa 10 km/litr i pojemnością baku 50 litrów

my_car.add_fuel(40)  #tankowanie 40 litrów paliwa
my_car.drive(150)   #jazda przez 150 km
my_car.add_fuel(10)  #tankowanie 10 litrów paliwa
my_car.drive(200)   #jazda przez 200 km
my_car.add_fuel(10) #tankowanie 10 litrów paliwa
my_car.drive(240) #jazda przez 250 km
print(f"Poziom paliwa: {my_car.get_fuel_level()} litrów")
