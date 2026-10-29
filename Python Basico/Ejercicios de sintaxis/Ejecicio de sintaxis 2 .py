print ("--- Clasicador de Adultez ---")
name = input ("Ingrese su Nombre: ")
lastName = input ("Ingrese su Apellido: ")
age = int (input("Ingrese su edad cumplida: " ))


if age <= 5: 
    category = "Bebe 🟢"
    message = "Eres un Bebito"
elif age <= 10:
    category = "Preadolecente 🔵"
    message = "Ya le estas en la preadolecencia."
elif age <= 17:
    category = "Adolecente 🟣"
    message = "Eres un adolecente."
elif age <= 25:
    category ="Adulto Joven 🔴"
    message = "Eres un Adulto Joven."
elif age < 65:
    category ="Adulto 🔴"
    message = "Eres un Adulto."
elif age >= 65:
    category ="Adulto Mayor 🔴"
    message = "Eres un adulto Mayor, ya puedes pagar el autobus con la cedula!."
print (f"{name}, {lastName} tu categoría es: {category}")
print (message)
