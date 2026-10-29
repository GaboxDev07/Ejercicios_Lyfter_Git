
import csv


import os

print("Working directory:", os.getcwd())

print("Bienvenido al ejercicio extra de manejo de csvs")


def csv_reader_games_dev(read_path, developer):
    print("Bienvenidos al ejercicio extra de manejo de csvs 1")
    with open (read_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        print("These are the available games: ")
        for games in reader:
            if games[2] == developer:
                print(f"Name: {games[0]}")
                print(f"Genre: {games[1]}")
                print(f"Developer: {games[2]}")
                print(f"Classification: {games[3]}")
                print()


def main_reader_games_developer(read_path,developer):
    csv_reader_games_dev(read_path,developer)

main_reader_games_developer(
    input("Select the file you want to read: "),
    input("Enter the name of the developer: ").strip()
)