print ("Welcome to the Ejercicio extra de Funciones 3")

my_str = input("Enter a statement: ")


def vowels_checker(my_str):
    vowels_counter = 0
    for char in my_str:
        if char in "aeiou":
            vowels_counter += 1
    return vowels_counter


result = vowels_checker(my_str)
print (f"The Statement you enter has {result} vowels.")
