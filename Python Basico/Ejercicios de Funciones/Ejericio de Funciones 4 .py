print ("Welcome to the Ejercicio de Funciones 4")

text = "aicnalubma"
backwards_text = ""

def my_backwards_function(text):
    backwards_text = ""

    
    for char in range(len(text)-1,-1,-1):
        backwards_text = backwards_text  + text[char]
    return(backwards_text)


result = my_backwards_function(text)
print(result)