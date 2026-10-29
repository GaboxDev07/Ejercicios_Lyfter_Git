print("Welcome to the Ejercicio de Diccionarios 2")

list_keys = ["first_name", "last_name","role" ] 
list_values = ["Gabriel", "Venegas", "Student"]

personal_info = {}

for number in range (0, 3):
    personal_info[list_keys[number]] = list_values[number]

print (personal_info)