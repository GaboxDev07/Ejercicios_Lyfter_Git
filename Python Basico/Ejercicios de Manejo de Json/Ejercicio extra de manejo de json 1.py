print("Bienvenidos al ejercicio extra de manejo de json 1")

import json
import os

def pokedex_read_json(read_path):
    read_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), read_path)
    with open(read_path,'r', encoding='utf-8')as file:
        pokedex = json.load(file)
        return pokedex


def main_pokedex_reader(read_path):
    current_pokedex = pokedex_read_json(read_path)
    for pokemon in current_pokedex:
        print (f"Name: {pokemon['name']}")
        print (f"Type: {pokemon['type']}")
        print (f"Level: {pokemon['level']}")
        print (f"Shiny: {pokemon['is_shiny']}")
        print("")

main_pokedex_reader(
    input("Enter the name of the file you want to read: ")
)

