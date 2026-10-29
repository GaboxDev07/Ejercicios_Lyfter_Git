print("Welcome to the Ejercicio extra de Diccionarios 2")

employees = [
    { 
    "name": "Carlos", 
    "email": "carlos@empresa.com", 
    "department": "Ventas"
    },

    {
    "name": "Ana",
    "email": "ana@empresa.com", 
    "department": "TI"
    },

    {
    "name": "Luis",
    "email": "luis@empresa.com", 
    "department": "Ventas"
    },

    {
    "name": "Sofia",
    "email": "sofia@empresa.com", 
    "department": "RRHH"
    },
]

grouped_employees = {}

for employee in employees:
    name = employee['name']

    if employee['department'] in grouped_employees:
        grouped_employees[employee['department']].append(name)

    else: 
        grouped_employees[employee['department']] = [name]
print(grouped_employees)

