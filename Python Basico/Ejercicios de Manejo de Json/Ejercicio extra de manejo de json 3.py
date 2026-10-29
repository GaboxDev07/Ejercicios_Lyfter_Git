print("Bienvenidos al ejercicio extra de manejo de json 3")

import json
import os

def pokedex_read_json(read_path):
    read_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), read_path)
    with open(read_path,'r', encoding='utf-8')as file:
        pokedex = json.load(file)
        return pokedex

def main_poke_stats_reader(read_path):
    current_pokedex = pokedex_read_json(read_path)
    for pokemon in current_pokedex:
        stats = pokemon['stats']
        print(f"Name: {pokemon['name']}")
        print (f"HP: {stats['hp']}")
        print (f"Attack: {stats['attack']}")
        print (f"Def: {stats['defense']}")
        print (f"SpAtk: {stats['sp_attack']}")
        print (f"SpDef: {stats['sp_defense']}")
        print (f"Speed: {stats['speed']}")
        print("")


main_poke_stats_reader(
    input("Enter the name of the file you want to read: ")
)