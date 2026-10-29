print ("Welcome to the Ejercicio de Funciones 3")

numbers = [8, 9, 25, 33, 40]

def sum_numbers_of_numbers (numbers):
    total = 0
    
    for number  in numbers:
        total = total + number
    return(total)

result = sum_numbers_of_numbers(numbers)

print(result)