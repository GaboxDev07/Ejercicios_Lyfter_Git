print ("Welcome to the Ejercicio de Funciones 5")

word = "Dragon Ball Z"


def my_upper_lower_case_checker (word):
    upper_cases = 0
    lower_cases = 0

    
    for char in word:
        if char.isupper():
            upper_cases = upper_cases + 1
        if char.islower():
            lower_cases = lower_cases + 1


    print(f"There are {upper_cases} upper cases and {lower_cases} lower cases"  )
    
my_upper_lower_case_checker(word)
