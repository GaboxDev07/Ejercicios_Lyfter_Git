print ("Welcome to the Ejercicio de Funciones 2.2")

this_is_a_global_variable = 15

def my_function_to_access_the_global_variable():
    global this_is_a_global_variable
    this_is_a_global_variable = 30
    print (f"Thi is printing the global variable modified: {this_is_a_global_variable}")



my_function_to_access_the_global_variable()
print(this_is_a_global_variable)
