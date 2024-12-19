"""
Napisz program, który rekurencyjnie i 
iteracyjnie szuka w napisie (w zależności od tego, czego chce użytkownik):
spółgłosek, samogłosek, cyfr i znaków specjalnych. 
Na końcu zwróć ich ilość oraz czas potrzebny do wyznaczenia. 
Wygeneruj losowe napisy o długości zadanej przez użytkownika.
"""

import random
import string
import time

def generate_random_string(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

def count_vowels_iterative(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char in vowels:
            count += 1
    return count

def count_consonants_iterative(s):
    vowels = "aeiouAEIOU"
    count = 0
    for char in s:
        if char.isalpha() and char not in vowels:
            count += 1
    return count

def count_digits_iterative(s):
    count = 0
    for char in s:
        if char.isdigit():
            count += 1
    return count

def count_special_chars_iterative(s):
    count = 0
    for char in s:
        if not char.isalnum():
            count += 1
    return count

def count_vowels_recursive(s):
    if not s:
        return 0
    return (1 if s[0] in "aeiouAEIOU" else 0) + count_vowels_recursive(s[1:])

def count_consonants_recursive(s):
    if not s:
        return 0
    return (1 if s[0].isalpha() and s[0] not in "aeiouAEIOU" else 0) + count_consonants_recursive(s[1:])

def count_digits_recursive(s):
    if not s:
        return 0
    return (1 if s[0].isdigit() else 0) + count_digits_recursive(s[1:])

def count_special_chars_recursive(s):
    if not s:
        return 0
    return (1 if not s[0].isalnum() else 0) + count_special_chars_recursive(s[1:])

def main():
    length = int(input("Podaj długość napisu: "))
    random_string = generate_random_string(length)
    print(f"Wygenerowany napis: {random_string}")

    choice = input("Co chcesz policzyć? (spółgłoski, samogłoski, cyfry, znaki specjalne): ").strip().lower()
    method = input("Wybierz metodę (iteracyjnie, rekurencyjnie): ").strip().lower()

    start_time = time.time()

    if choice == "samogłoski":
        if method == "iteracyjnie":
            count = count_vowels_iterative(random_string)
        elif method == "rekurencyjnie":
            count = count_vowels_recursive(random_string)
    elif choice == "spółgłoski":
        if method == "iteracyjnie":
            count = count_consonants_iterative(random_string)
        elif method == "rekurencyjnie":
            count = count_consonants_recursive(random_string)
    elif choice == "cyfry":
        if method == "iteracyjnie":
            count = count_digits_iterative(random_string)
        elif method == "rekurencyjnie":
            count = count_digits_recursive(random_string)
    elif choice == "znaki specjalne":
        if method == "iteracyjnie":
            count = count_special_chars_iterative(random_string)
        elif method == "rekurencyjnie":
            count = count_special_chars_recursive(random_string)
    else:
        print("Nieprawidłowy wybór.")
        return

    end_time = time.time()
    elapsed_time = end_time - start_time

    print(f"Liczba {choice}: {count}")
    print(f"Czas potrzebny do wyznaczenia: {elapsed_time:.6f} sekund")

if __name__ == "__main__":
    main()