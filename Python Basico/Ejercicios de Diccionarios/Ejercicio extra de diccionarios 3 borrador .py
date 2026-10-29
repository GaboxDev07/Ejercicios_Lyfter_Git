print("Welcome to the Ejercicio extra de Diccionarios 2")

products = [
    {"name": "Monitor", 
    "category": "Electrónica", 
    "price": 200},
    
    {"name": "Teclado", 
    "category": "Electrónica",
    "price": 50},
    
    {"name": "Silla",
    "category": "Muebles",
    "price": 120},
    
    {"name": "Mesa",
    "category": "Muebles", 
    "price": 180},
    
    {"name": "Mouse", 
    "category": "Electrónica", 
    "price": 25},
]
total_by_category = {}

for product in products:
    print(product['category'])
    if product['category'] in total_by_category:
        total_by_category[product['category']] = total_by_category[product['category']] + product['price']
        
    else:
        total_by_category[product['category']] = product['price']
        
print("The total amount per category is: ", total_by_category)

