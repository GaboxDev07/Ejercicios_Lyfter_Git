import csv
import os

print("Working directory:", os.getcwd())
print("Script directory:", os.path.dirname(os.path.abspath(__file__)))


def csv_reader_games(read_path):
    print("Bienvenidos al ejercicio extra de manejo de csvs 1")
    read_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), read_path)
    with open (read_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        print("These are the available games: ")
        for games in reader:
            print(f"Name: {games[0]}")
            print(f"Genre: {games[1]}")
            print(f"Developer: {games[2]}")
            print(f"Classification: {games[3]}")
            print()


def main_reader_games(read_path):
    csv_reader_games(read_path)

main_reader_games(
    input("Select the file you want to read: ")
)