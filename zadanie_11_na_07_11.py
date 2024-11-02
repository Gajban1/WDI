"""
Zadanie 11.
Wykorzystując odwzorowanie list (ang. list comprehension)
 proszę porównać ze sobą kolejne elementy dwóch wcześniej 
 wygenerowanych list (jak w poprzednich zadaniach). 
 Jeśli elementy są równe do nowej listy należy wpisać True,
   w przeciwnym wypadku False. Na koniec należy wybrać elementy o 
   wartości False z jednej z początkowych list ponownie korzystając 
   z mechanizmu odwzorowania list. Dla porównania można skorzystać z 
   metody itertools.compress().

"""
from random import randint
from itertools import compress

def generowanie_listy(N,M,L):
    tem = [randint(L, M) for _ in range(N)]
    return tem
    

print("""
    Podaj następujace wartości po spacji:
      N - ilość elementów do wygenerowania
      M - górna granica zakresu
      L - dolna granica zakresu
      """)
try:
    b = list(map(int, input("Podaj N, M, L po spacji: ").split()))

    #print(b)
    randomlist1 = generowanie_listy(b[0], b[1], b[2])
    randomlist2 = generowanie_listy(b[0], b[1], b[2])
except:
    print("Podano nieprawidłowy format danych :D")
    exit()

#Wyświetlenie wygenerowanych tablic
print(f"Pierwsza Wygenerowana tablica: {randomlist1} \n Druga wygenerowana tablica: {randomlist2}")

#Porównywanie elemntów listy
first_operation = [randomlist1[x] == randomlist2[x] for x in range(0, len(randomlist1))]
print(first_operation)

#Wypisywanie elementów dla których operacja porównania wskazuje na False
second_operation = [randomlist1[x] for x in range(0,len(randomlist1)) if first_operation[x] == False]
print(second_operation)

#Dla porówania gotowa funckja z biblioteki itertools
cus = compress(randomlist1, [x==False for x in first_operation])
for i in cus:
    print(i)