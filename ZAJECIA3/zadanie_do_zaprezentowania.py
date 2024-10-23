# NR 6 Napisać program sprawdzający czy zadana liczba jest pierwsza.


def czy_pierwsza(a):
    n = 1
    dzielniki = 0
    while n <= a**(1/2):
        if a % n == 0:
            dzielniki += n
        n+=1
    
    return True if dzielniki == 1 else False

def main():
    try: 
        a = int(input("Wprowadz liczbe: "))
        print(czy_pierwsza(a))
    except:
        print("Wprowadzona wartość nie jest liczbą naturalną")

main()