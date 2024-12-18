import unittest
from zadania_na_klasy import Zadanie

class TestTrapezIstnieje(unittest.TestCase):

    def setUp(self):
        self.zadanie = Zadanie()

    def test_trapez_istnieje_dane1(self):
        dane1 = [(0, 0), (4, 0), (1, 3), (3, 3)]  # Trapez istnieje
        self.assertTrue(self.zadanie.trapez_istnieje(dane1), "Test 1 powiódł się")

    def test_trapez_istnieje_dane2(self):
        dane2 = [(0, 0), (5, 0), (1, 2), (4, 2)]  # Trapez istnieje
        self.assertTrue(self.zadanie.trapez_istnieje(dane2), "Test 2 powiódł się")

    def test_trapez_istnieje_dane3(self):
        dane3 = [(0, 0), (4, 0), (1, 2), (3, 2)]  # Trapez nie istnieje
        self.assertTrue(self.zadanie.trapez_istnieje(dane3), "Test 3 nie powiódł się")

    def test_trapez_istnieje_dane4(self):
        dane4 = [(0, 0), (4, 0), (1, 1), (3, 1)]  # Trapez nie istnieje
        self.assertTrue(self.zadanie.trapez_istnieje(dane4), "Test 4 nie powiódł się")

    def test_trapez_istnieje_dane5(self):
        dane5 = [(0, 0), (4, 0), (1, 0), (3, 0)]  # Trapez nie istnieje
        self.assertTrue(self.zadanie.trapez_istnieje(dane5), "Test 5 nie powiódł się")

    def test_trapez_istnieje_dane6(self):
        dane6 = [(0, 0), (4, 0), (1, 3), (3, 3)]  # Trapez istnieje
        self.assertTrue(self.zadanie.trapez_istnieje(dane6), "Test 6 powiódł się")

    def test_trapez_istnieje_dane7(self):
        dane7 = [(0, 0), (4, 0), (1, 2), (3, 2), (2, 1)]  # Punkt (2, 1) leży wewnątrz
        self.assertFalse(self.zadanie.trapez_istnieje(dane7), "Test 7 nie powiódł się")

    def test_trapez_istnieje_dane8(self):
        dane8 = [(1,1), (1,2), (2,1), (3,0), (3,3), (2,2)]  # Trapez istnieje
        self.assertTrue(self.zadanie.trapez_istnieje(dane8), "Test 8 powiódł się")

    def test_trapez_istnieje_dane9(self):
        dane9 = [
            (2, 2), (6, 2), (3, 5), (5, 5),  # Punkty trapezu
            (0, 0), (7, 1), (8, 6), (4, 7), (1, 8), (6, 9), (9, 3), (3, 10), (10, 0), (0, 9)
        ]  # Trapez istnieje
        self.assertTrue(self.zadanie.trapez_istnieje(dane9), "Test 9 powiódł się")

    def test_trapez_istnieje_dane10(self):
        dane10 = [
            (2, 2), (8, 2), (4, 6), (6, 6),  # Punkty trapezu
            (3, 4), (5, 5), (7, 4), (5, 3), (4, 5),  # Punkty wewnątrz trapezu
            (0, 0), (9, 7), (10, 1), (1, 9), (8, 10)  # Punkty na zewnątrz trapezu
        ]  # Trapez nie istnieje
        self.assertFalse(self.zadanie.trapez_istnieje(dane10), "Test 10 nie powiódł się")

if __name__ == "__main__":
    unittest.main()