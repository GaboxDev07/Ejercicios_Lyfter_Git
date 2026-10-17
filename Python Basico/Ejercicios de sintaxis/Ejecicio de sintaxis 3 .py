import random

print("--- Binevenidos al juego de adivina el numero ---")
print ("Si quiere abandonar precione ctrl + c")

random_number = random.randint(1,10)
selected_secret_number = int(input("Ingrese un numero del 1 al 10: "))

while random_number != selected_secret_number: 
    selected_secret_number = int(input("No ha adivinado, intente de nuevo: "))
print ("Adivinaste el numero secreto ", random_number)
print ("El Juego ha terminado")
print("Felicidades ud ha ganado!")





