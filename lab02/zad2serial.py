import pickle
from punkt import Punkt
from nazwanypunkt import NazwanyPunkt

# Tworzenie obiektów Punkt i NazwanyPunkt
punkt1 = Punkt(1, 2)
punkt2 = Punkt(3, 4)
nazwany_punkt1 = NazwanyPunkt(5, 6, "A")
nazwany_punkt2 = NazwanyPunkt(7, 8, "B")

# Tworzenie listy obiektów
punkty = [punkt1, punkt2, nazwany_punkt1, nazwany_punkt2]

# Zapisywanie listy do pliku punkty.pkl
with open("punkty.pkl", "wb") as file:
    pickle.dump(punkty, file)


# Odczytywanie listy z pliku punkty.pkl
with open("punkty.pkl", "rb") as file:
    wczytane_punkty = pickle.load(file)

# Wyświetlenie wczytanych punktów
for punkt in wczytane_punkty:
    print(punkt)

