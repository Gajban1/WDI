import pytest
from zadania_na_klasy import Zadanie



@pytest.fixture
def zadanie():
    return Zadanie()

def test_trapez_istnieje_dane1(zadanie):
    dane1 = [(0, 0), (4, 0), (1, 3), (3, 3)]  # Trapez istnieje
    assert zadanie.trapez_istnieje(dane1) == True, "Test 1 powiódł się"

def test_trapez_istnieje_dane2(zadanie):
    dane2 = [(0, 0), (5, 0), (1, 2), (4, 2)]  # Trapez istnieje
    assert zadanie.trapez_istnieje(dane2) == True, "Test 2 powiódł się"

def test_trapez_istnieje_dane3(zadanie):
    dane3 = [(0, 0), (4, 0), (1, 3), (3, 3), (2, 2)]  # Punkt wewnątrz trapezu
    assert zadanie.trapez_istnieje(dane3) == False, "Test 3 nie powiódł się"

def test_trapez_istnieje_dane4(zadanie):
    dane4 = [(0, 0), (4, 0), (0, 3), (4, 3)]  # Brak równoległych boków
    assert zadanie.trapez_istnieje(dane4) == False, "Test 4 nie powiódł się"

def test_trapez_istnieje_dane5(zadanie):
    dane5 = [(0, 0), (4, 0), (2, 2)]  # Za mało punktów
    assert zadanie.trapez_istnieje(dane5) == False, "Test 5 nie powiódł się"

def test_trapez_istnieje_dane6(zadanie):
    dane6 = [
        (0, 0), (4, 0), (1, 3), (3, 3),  # Punkty trapezu
        (-1, -1), (5, -1), (5, 4), (-1, 4)  # Punkty poza trapezem
    ]
    assert zadanie.trapez_istnieje(dane6) == True, "Test 6 powiódł się"

def test_trapez_istnieje_dane7(zadanie):
    dane7 = [(0, 0), (4, 0), (1, 2), (3, 2), (2, 1)]  # Punkt (2, 1) leży wewnątrz
    assert zadanie.trapez_istnieje(dane7) == False, "Test 7 nie powiódł się"

def test_trapez_istnieje_dane8(zadanie):
    dane8 = [(1,1), (1,2), (2,1), (3,0), (3,3), (2,2)]
    assert zadanie.trapez_istnieje(dane8) == True, "Test 8 powiódł się"

def test_trapez_istnieje_dane9(zadanie):
    dane9 = [
        (2, 2), (6, 2), (3, 5), (5, 5),  # Punkty trapezu
        (0, 0), (7, 1), (8, 6), (4, 7), (1, 8), (6, 9), (9, 3), (3, 10), (10, 0), (0, 9)
    ]
    assert zadanie.trapez_istnieje(dane9) == True, "Test 9 powiódł się"

def test_trapez_istnieje_dane10(zadanie):
    dane10 = [
        (2, 2), (8, 2), (4, 6), (6, 6),  # Punkty trapezu
        (3, 4), (5, 5), (7, 4), (5, 3), (4, 5),  # Punkty wewnątrz trapezu
        (0, 0), (9, 7), (10, 1), (1, 9), (8, 10)  # Punkty na zewnątrz trapezu
    ]
    assert zadanie.trapez_istnieje(dane10) == False, "Test 10 nie powiódł się"

# Run tests:
if __name__ == '__main__':
    pytest.main() 