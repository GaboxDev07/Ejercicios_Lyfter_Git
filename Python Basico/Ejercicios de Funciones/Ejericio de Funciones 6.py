print ("Welcome to the Ejercicio de Funciones 6")

word_with_hyphens = "python-variable-funcion-computadora-monitor-teclado-mouse-parlantes-audifonos"


def my_string_with_hyphens(word_with_hyphens):
    words = word_with_hyphens.split("-")
    words.sort()
    ordered_text = "-".join(words)
    return(ordered_text)

result = my_string_with_hyphens(word_with_hyphens)
print(result)
