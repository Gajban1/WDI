import random


def rysuj_choinke(wysokosc):

    print(" " * (wysokosc - 1) + "X")
    
    # Rysowanie reszty choinki
    for i in range(wysokosc):

        if i == 0:
            continue
        spacje = " " * (wysokosc - i - 1)
        

        srodek = ["*"] * (2 * i + 1)  # Lista gwiazdek dla bieżącej linii
        

        liczba_bombek = random.randint(0, len(srodek)//2)
        pozycje_bombek = random.sample(range(len(srodek)), liczba_bombek)  # Losowe pozycje
        
        # Umieszczamy bombki "o" w losowych miejscach
        for pozycja in pozycje_bombek:
            srodek[pozycja] = "o"
        

        print(spacje + "".join(srodek))
    

    print(" " * (wysokosc - 1) + "U")


wysokosc = int(input("Podaj wysokość choinki: "))


rysuj_choinke(wysokosc)
