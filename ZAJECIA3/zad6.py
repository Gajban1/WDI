a = float(input("Podaj pierwszą liczbę: "))
b = float(input("Podaj drugą liczbę: "))

# Sprawdzenie czy obie liczby są mniejsze od 0
if a < 0 and b < 0:
    # Zakończenie programu, jeśli obie liczby są mniejsze od 0
    print("Obie liczby są mniejsze od zera. Program zakończony.")
else:
    # Jeśli tylko jedna liczba jest mniejsza od 0, należy użyć jej wartości bezwzględnej
    if a < 0:
        a = abs(a)  # Użycie wartości bezwzględnej dla liczby a
        print("Użyto wartości bezwzględnej dla pierwszej liczby.")
    if b < 0:
        b = abs(b)  # Użycie wartości bezwzględnej dla liczby b
        print("Użyto wartości bezwzględnej dla drugiej liczby.")

    # Obliczenia
    suma = a + b
    roznica = a - b
    iloczyn = a * b
    iloraz = a / b if b != 0 else "Nie można dzielić przez zero"  # Sprawdzenie, czy dzielenie przez zero
    kwadrat_a = a ** 2
    kwadrat_b = b ** 2
    pierwiastek_a = a ** 0.5
    pierwiastek_b = b ** 0.5

    # Wyniki
    print(f"Suma liczb: {suma}")
    print(f"Różnica liczb: {roznica}")
    print(f"Iloczyn liczb: {iloczyn}")
    
    # Dodatkowy komunikat, jeśli wynik iloczynu wynosi 10
    if iloczyn == 10:
        print("Yay!")
    
    print(f"Iloraz liczb: {iloraz}")
    print(f"Kwadrat pierwszej liczby: {kwadrat_a}")
    print(f"Kwadrat drugiej liczby: {kwadrat_b}")
    print(f"Pierwiastek drugiego stopnia z pierwszej liczby: {pierwiastek_a}")
    print(f"Pierwiastek drugiego stopnia z drugiej liczby: {pierwiastek_b}")
