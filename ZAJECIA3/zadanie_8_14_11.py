"""
Proszę napisać 
program wczytujący tablicę dwuwymiarową o ustalonym wymiarze 
 wypełnioną liczbami naturalnymi. Dla danej tablicy należy napisać 
 funkcję, która będzie odpowiadała na pytanie, czy w tablicy każdy wiersz 
 zawiera co najmniej jedną liczbą złożoną 
 wyłącznie z cyfr będących liczbami pierwszymi. 
 Wymiar tablicy powinien być definiowany przez użytkownika.
 """

from random import randint

def sprawdz_pierwsze(a):
    pierwsze = ["2", "3", "5","7"]
    tem = 0
    ile = 0
    for i in a:
        i  = str(i)
        for t in i:
            if t in pierwsze:
                tem += 1
                continue
            else:
                break
        if tem == len(i):
            ile += 1
        


    return ile >= 1


try:
    ile_wierszy = 0
    n = int(input("Podaj wymar tabliy nxn: "))

    tablica = [[randint(1,100000) for _ in range(n)] for _ in range(n)]
    #tablica = [[3337,12341],[3577,134141]] Przyklad

    for i in tablica:
        if sprawdz_pierwsze(i):
            ile_wierszy += 1
        
    if ile_wierszy == len(tablica):
        print("W kazdym wierszu znajduje sie conajmniej jedna cyfra skladajaca z cyfr pierwszych")
    else:
        print("Nie w kazdym wierszu znajduje sie conajmniej jedna cyfra skladajaca z cyfr pierwszych")


except:
    print("Podano nie prawidłowy format danych")