import csv

def count_games_by_genre(read_path):
    print("Bienvenidos al ejercicio extra de manejo de csvs 1")
    with open (read_path, 'r', encoding='utf-8') as file:
        reader = csv.reader(file)
        headers = next(reader)
        genre_counter = {}
        for games in reader:
            genre = games[1]

            if genre in genre_counter:
                genre_counter[genre] += 1

            else:
                genre_counter[genre] = 1

        print("Genres found:")
        for genre, count in sorted(genre_counter.items()):
            print(f"{genre}: {count} ")

def main_count_games_by_genre(read_path):
    count_games_by_genre(read_path)

main_count_games_by_genre(
    input("Select the file you want to read: ")
)
