print ("Welcome to the Ejercicio de Funciones 7")

numbers = [ 1, 3, 5, 7, 8, 9, 10, 13, 17, 19, 22, 25, 29, 30, 33, 35, 36]

def check_if_prime_number(number):
    is_prime = True
    for divisor in range(2, number):
        if number % divisor == 0:
            is_prime = False
    return(is_prime)

def check_for_prime_numbers(numbers):
    prime_numbers = []
    for number in numbers:
        if check_if_prime_number(number):
            prime_numbers.append(number)
    return(prime_numbers)


result = check_for_prime_numbers(numbers)
print("This is the list of prime numbers: ", result)

