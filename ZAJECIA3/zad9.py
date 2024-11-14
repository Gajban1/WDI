"""
Stworzyć aplikację symulującą bankomat i wpłatomat.
Użytkownik może wykonać trzy operacje: wpłata, wypłata, sprawdzić saldo.
Należy przechowywać saldo.
Przed każdą operacją należy zapytać użytkownika o PIN.
Użytkownik nie może wybrać większej kwoty niż ta na koncie.
Użytkowanie rozpoczyna się od podania typu operacji.
Po każdej operacji powinien zostać wypisany komunikat: “Co chcesz zrobić w kolejnym kroku?”. (Użytkownik może też zakończyć korzystanie z programu).

"""

import os
clear = lambda: os.system('clear')

stan = 0
flag = True
pin = 1111

def deposit():
    clear()

    t = int(input("Podaj kwote do wpłaty: "))
    local_var = stan + t
    return local_var

def withdraw():
    clear()

    t = int(input("Ile chcesz wypłacić: "))
    if t <= stan:
        return t
    else:
        print("Masz za mało kasiory")
        return 0 

def main():
    global stan
    global flag
    global pin

    print("""Wybierz operacje:
          1. Wpłata
          2. Wypłata
          3. Stan konta
          4. Wyjście """)
    opt = int(input("       WYBRANO: "))
    
    match opt:
        case 1:
            ppin = int(input("PODAJ PIN: "))
            if ppin == pin:
                stan = deposit()
            else:
                clear()
                print("NIE POPRAWNY PIN")
        case 2:
            ppin = int(input("PODAJ PIN: "))
            if ppin == pin:

                stan -= withdraw()

            else:
                clear()
                print("NIE POPRAWNY PIN")
        case 3:
            clear()
            print(f"Twój aktualny stan konta: {stan}")
        case 4:
            flag = False


while flag:
    try:
        main()
    except:
        clear()
        print("Podana złą wartość")




