print("Welcome to the Ejercicio de Diccionarios 3")

deleted_keys = ['access_level','age',]

employee = {'name':'Gabriel', 'email': 'gabox@ecorp.com', 'access_level':5, 'age': 31}

for key in deleted_keys:
    employee.pop(key)

print(employee)