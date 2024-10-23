import random
import math

def calculator():
    while True:
        try:
            num1 = float(input("Podaj pierwszą liczbę: "))
            num2 = None
            operator = input("Podaj operator (+, -, *, /, ^, #, x): ")

            if operator in ['+', '-', '*', '/']:
                num2 = float(input("Podaj drugą liczbę: "))

            if operator == '+':
                wynik = num1 + num2
                print(f"Wynik: {wynik}")
            elif operator == '-':
                wynik = num1 - num2
                print(f"Wynik: {wynik}")
            elif operator == '*':
                wynik = num1 * num2
                print(f"Wynik: {wynik}")
            elif operator == '/':
                if num2 != 0:
                    wynik = num1 / num2
                    print(f"Wynik: {wynik}")
                else:
                    print("Błąd: dzielenie przez zero!")
            elif operator == '^':
                wynik = num1 ** 2
                print(f"Wynik: {wynik}")
            elif operator == '#':
                if num1 >= 0:
                    wynik = math.sqrt(num1)
                    print(f"Wynik: {wynik}")
                else:
                    print("Błąd: nie można obliczyć pierwiastka z liczby ujemnej!")
            elif operator == 'x':
                min_val = int(input("Podaj minimalną wartość zakresu: "))
                max_val = int(input("Podaj maksymalną wartość zakresu: "))
                wynik = random.randint(min_val, max_val)
                print(f"Wylosowana liczba: {wynik}")
            else:
                print("Nieznany operator!")

        except ValueError:
            print("Błąd: nieprawidłowe dane wejściowe!")

        restart = input("Czy chcesz wprowadzić nowe dane? (T/N): ").strip().upper()
        if restart != 'T':
            print("Kalkulator zakończył działanie.")
            break

calculator()
