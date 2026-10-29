print("Bienvenidos al ejercicio extra de manejo de json 4")


import json
import os

def pokedex_read_json(read_path):
    read_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), read_path)
    with open(read_path,'r', encoding='utf-8')as file:
        pokedex = json.load(file)
        return pokedex

def poke_type_reader(read_path):
    current_pokedex = pokedex_read_json(read_path)

    pokemon_type_counter = {}
    pokemon_level_counter = {}

    for pokemon in current_pokedex:
        pokemon_type = pokemon['type']
        pokemon_level = pokemon['level']

        if pokemon_type in pokemon_type_counter:
            pokemon_type_counter[pokemon_type] += 1
        else:
            pokemon_type_counter[pokemon_type] = 1


        if pokemon_type in pokemon_level_counter:
            pokemon_level_counter[pokemon_type] += pokemon_level
        else: 
            pokemon_level_counter[pokemon_type] = pokemon_level
    return pokemon_type_counter, pokemon_level_counter

def average_level_per_type(pokemon_type_counter,pokemon_level_counter):
    for pokemon_type in pokemon_type_counter:
        current_type_count = pokemon_type_counter[pokemon_type]
        current_level_count = pokemon_level_counter[pokemon_type]
        average_level = current_level_count / current_type_count
        print(f"{pokemon_type} it's average Level is: {average_level}")

def main_average_level_per_type(read_path):
    pokemon_type_counter,pokemon_level_counter = poke_type_reader(read_path)
    average_level_per_type(pokemon_type_counter,pokemon_level_counter)

main_average_level_per_type(   
    input("Select the file you want to read: ")
)

