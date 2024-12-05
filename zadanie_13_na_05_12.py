from itertools import combinations
import matplotlib.pyplot as plt

def pole_trojkata(p1, p2, p3):
    return abs(
        p1[0] * (p2[1] - p3[1]) +
        p2[0] * (p3[1] - p1[1]) +
        p3[0] * (p1[1] - p2[1])
    ) / 2

def punkt_w_trapezie(punkt, p1, p2, p3, p4):
    """Sprawdza, czy dany punkt znajduje się wewnątrz trapezu."""
    # Obliczamy pole trapezu jako sumę dwóch trójkątów
    pole_trapezu = pole_trojkata(p1, p2, p3) + pole_trojkata(p1, p3, p4)
    
    # Obliczamy sumę pól trójkątów złożonych z punktu i wierzchołków trapezu
    suma_poli = (
        pole_trojkata(punkt, p1, p2) +
        pole_trojkata(punkt, p2, p3) +
        pole_trojkata(punkt, p3, p4) +
        pole_trojkata(punkt, p4, p1)
    )
    
    # Punkt jest wewnątrz trapezu, jeśli suma pól jest równa polu trapezu
    return False if (suma_poli - pole_trapezu) >= 0 else True

def czy_rownolegle(p1, p2, p3, p4):
    """Sprawdza, czy dwie linie są równoległe."""
    def wspolczynnik_kierunkowy(p1, p2):
        if p1[0] == p2[0]:  # Linia pionowa
            return 1
        return (p2[1] - p1[1]) / (p2[0] - p1[0])
    
    m1 = wspolczynnik_kierunkowy(p1, p2)
    m2 = wspolczynnik_kierunkowy(p3, p4)
    return True if int(m1 - m2) == 0 or (m1 == "pionowa" and m2 == "pionowa") else False

def trapez_istnieje(dane):
    """Sprawdza, czy można utworzyć trapez i zwraca wierzchołki trapezu."""
    if len(dane) < 4:
        return False

    for p1, p2, p3, p4 in combinations(dane, 4):
        
        if czy_rownolegle(p1, p2, p3, p4):

            dlug1 = ((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)**(1/2)
            dlug2 = ((p3[0] - p4[0])**2 + (p3[1] - p4[1])**2)**(1/2)

            if dlug1 != dlug2:
                punkty_wewnatrz = [
                punkt for punkt in dane
                if punkt not in [p1, p2, p3, p4] and punkt_w_trapezie(punkt, p1, p2, p3, p4)
            
            ]
                if len(punkty_wewnatrz) == 0:
                    return True
                else:
                    return False
            
        if czy_rownolegle(p1, p4, p2, p3):
              dlug1 = ((p1[0] - p4[0])**2 + (p1[1] - p4[1])**2)**(1/2)
              dlug2 = ((p2[0] - p3[0])**2 + (p2[1] - p3[1])**2)**(1/2)

              if dlug1 != dlug2:
                punkty_wewnatrz = [punkt for punkt in dane if punkt not in [p1, p2, p3, p4] and punkt_w_trapezie(punkt, p1, p2, p3, p4)]
                if len(punkty_wewnatrz) == 0:
                    return True
                else:
                    return False
                
    return False

def wizualizuj_punkty(dane, opis="TEST 1"):
    """Wizualizuje punkty na płaszczyźnie."""
    x = [p[0] for p in dane]
    y = [p[1] for p in dane]
    
    plt.scatter(x, y, color='blue')
    
    for i, punkt in enumerate(dane):
        plt.annotate(f'P{i}', (punkt[0], punkt[1]), textcoords="offset points", xytext=(0,10), ha='center')
    

    
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title(opis)
    plt.grid(True)
    plt.show()


# Testy
def test_trapez_istnieje():
    # Testy pozytywne
    dane1 = [(0, 0), (4, 0), (1, 3), (3, 3)]  # Trapez istnieje
    dane2 = [(0, 0), (5, 0), (1, 2), (4, 2)]  # Trapez istnieje

    # Testy negatywne
    dane3 = [(0, 0), (4, 0), (1, 3), (3, 3), (2, 2)]  # Punkt wewnątrz trapezu
    dane4 = [(0, 0), (4, 0), (0, 3), (4, 3)]  # Brak równoległych boków
    dane5 = [(0, 0), (4, 0), (2, 2)]  # Za mało punktów

    # Test dla punktów poza trapezem
    dane6 = [
        (0, 0), (4, 0), (1, 3), (3, 3),  # Punkty trapezu
        (-1, -1), (5, -1), (5, 4), (-1, 4)  # Punkty poza trapezem
    ]

    # Test trapezu ukośnego
    dane7 = [(0, 0), (4, 0), (1, 2), (3, 2), (2, 1)]  # Punkt (2, 1) leży wewnątrz

    dane8 = [(1,1), (1,2), (2,1), (3,0), (3,3), (2,2)]

    assert trapez_istnieje(dane1) == True, "Test 1  powiódł się"
    assert trapez_istnieje(dane2) == True, "Test 2  powiódł się"
    assert trapez_istnieje(dane3) == False, "Test 3 nie powiódł się"
    assert trapez_istnieje(dane4) == False, "Test 4 nie powiódł się"
    assert trapez_istnieje(dane5) == False, "Test 5 nie powiódł się"
    assert trapez_istnieje(dane6) == True, "Test 6  powiódł się"
    assert trapez_istnieje(dane7) == False, "Test 7 nie powiódł się"
    assert trapez_istnieje(dane8) == True, "Test 8  powiódł się"

    print("Wszystkie testy przeszły pomyślnie!")

    # Wizualizacja punktów dla każdego zestawu danych
    #wizualizuj_punkty(dane1, "TEST 1")
    #wizualizuj_punkty(dane2, "TEST 2")
    #wizualizuj_punkty(dane3, "TEST 3")
    #wizualizuj_punkty(dane4, "TEST 4")
    #wizualizuj_punkty(dane5, "TEST 5")
    #wizualizuj_punkty(dane6, "TEST 6" )
    #wizualizuj_punkty(dane7, "TEST 7")
    wizualizuj_punkty(dane8 , "TEST 8")

# Uruchomienie testów
test_trapez_istnieje()
