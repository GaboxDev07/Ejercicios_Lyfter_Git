print("--- Binevenidos a cual numero es el mayor ---")

number1 = int (input ("Ingrese 3 numeros del 1 al 100: "))
number2 = int (input ("Ingrese 3 numeros del 1 al 100: "))
number3 = int (input ("Ingrese 3 numeros del 1 al 100: "))

if number1 > number2 and number1 > number3:
    print (number1)

elif number2 > number1 and number2 > number3:
    print (number2) 

elif number3 > number1 and number3 > number2:
    print (number3) 

