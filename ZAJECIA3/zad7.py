"""
Należy wypisać liczby z zakresu przedstawionego przez użytkownika.
    Aby zdefiniować zakres, użytkownik wprowadza 2 liczby.
    Po kolei, w kolejnych linijkach.
    Operujemy na liczbach całkowitych.
    Jeśli zakres jest większy niż 20, należy wypisać tylko 6 liczb z tego zakresu, które są najbliżej średniej (bez samej średniej).
    Program należy napisać z wykorzystaniem różnych pętli.
"""


def wypisz_zakres(a,b, p = float("inf")):
    for i in range(a, b+1):
        if i == p:
            continue
        print(i)

def srednia(a,b):
    suma = sum([i for i in range(a, b+1)])
    srs = suma // (abs(b-a)+1)
    wypisz_zakres(srs-3, srs+3, srs)


def main():
    start = int(input("Podaj poczatek: "))
    end = int(input("Podaj koniec: "))

    zakres = abs(end-start) +1

    if start < end:
        if zakres <= 20:
            wypisz_zakres(start,end)
        else:
            srednia(start, end)
        
    else: 
        print("Podano nie poprawny zakres")

while True:
    try:
        main()

        b = input("CZY ZAKONCZYC PROGRAM\n T/N\n")
        if b == "T" or b=="t":
            break
    except:
        print("Nie podano liczby calkowitej")