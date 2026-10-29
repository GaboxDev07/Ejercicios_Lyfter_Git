print ("Welcome to the Ejercicio de Funciones 2.1")

def my_define_variable():
    variable_inside_function_scope_test = 10
    print(f'This print is inside function: {variable_inside_function_scope_test}')


my_define_variable()


print(f"This print is outside the function: {variable_inside_function_scope_test}")


