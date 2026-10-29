print ("Bienvenido al ejercicio de manejo de Json 1")

import json
import os

def pokedex_read_json(read_path):
    read_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), read_path)
    with open(read_path, 'r', encoding='utf-8') as file:
        pokedex = json.load(file)
    return pokedex


def new_entry_pokedex(write_path, stats):
    with open (write_path, 'w', encoding='utf-8') as file:
        json.dump(stats, file , indent = 4 )


def get_number_of_pokemon():
    number_of_pokemon = int (input("How many pokemon you want to enter ?: "))
    return number_of_pokemon



def get_pokemon_stats(number_of_pokemon):

    stats_pokemon = []

    for number in range(number_of_pokemon):
        name = input("Enter the name: ")
        pokemon_type = input("Enter the type: ")
        level = int(input("Enter the level 1 - 100: "))
        is_shiny = input("Is shiny (True/False) : ").lower()
        if is_shiny == "true":
            is_shiny = True
        else:
            is_shiny = False

        item = input("Enter the item: ")
        attack1 = input("Enter the Move 1: ")
        attack2 = input("Enter the Move 2: ")
        attack3 = input("Enter the Move 3: ")
        attack4 = input("Enter the Move 4: ")
        hp = int(input("Enter the HP: "))
        attack = int(input("Enter the Atk: "))
        defense = int(input("Enter the Def: "))
        sp_attack = int(input("Enter the spAtk: "))
        sp_defense = int(input("Enter the spDef: "))
        speed = int(input("Enter the Speed: "))

        stats_pokemon.append({
            "name": name,
            "type": pokemon_type,
            "level": level,
            "is_shiny": is_shiny,
            "held_item": item,
            "skills":[
                 attack1,
                 attack2,
                 attack3,
                 attack4,
                    ],
            "stats":{
                "hp": hp,
                "attack": attack,
                "defense": defense,
                "sp_defense": sp_defense,
                "sp_attack": sp_attack,
                "speed": speed
                    }
        })
    return stats_pokemon





def main_pokedex():
    current_pokedex = pokedex_read_json("pokedex.json")

    number_of_pokemon = get_number_of_pokemon()

    new_pokemon = get_pokemon_stats(number_of_pokemon)

    current_pokedex.extend(new_pokemon)

    new_entry_pokedex("pokedex.json",current_pokedex)

    print(current_pokedex)

    return current_pokedex

if __name__ == "__main__":
    main_pokedex()

