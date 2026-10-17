print ("Welcome to the Ejercicio extra de Funciones 1")

word = input("Enter a word: ")
character = input("Enter the character you want to search: ")


def char_checker(word, character):
    char_counter = 0
    for char in word:
        if char == character:
            char_counter += 1       
    return(char_counter)


result = char_checker(word, character)
print(result)
