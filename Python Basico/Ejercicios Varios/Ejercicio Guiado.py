print ("--- Clasicador de nivel Gamer ---")
name = input ("Ingrese su nombre: ")
hours = int (input("Cuantas horas llevas jugando? " ))
is_competitive = input ("Juegas conpetitivo?" )

if hours < 10: 
    category = "Novato 🟢"
    message = "Bienvenido al mundo Gamer!"
elif hours < 50:
    category = "Casual 🔵"
    message = "Ya le estas agarrando el ritmo."
elif hours < 200:
    category = "Gamer 🟣"
    message = "Definitivamente sabes lo que haces."
elif hours >= 200:
    category ="Pro 🔴"
    message = "Eres una leyenda viviente."
else:
    category = "Gamer 🟣"
    message = "Tienes la experiencia, pero aun no entras al competitivo."

print (f"{name}, tu categoría es: {category}")
print (message)





