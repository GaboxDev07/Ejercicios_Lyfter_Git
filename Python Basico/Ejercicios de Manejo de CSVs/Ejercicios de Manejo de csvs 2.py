import csv


print("Bienvenidos al ejercicio de manejo de csvs 2")


def videogames_csv(write_path, data):
    with open(write_path,'w', encoding='utf-8', newline='' ) as file:
        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers, delimiter ='\t' )
        writer.writeheader()
        writer.writerows(data)

top_videogames = []

name = input("Enter the name of the video game: ")
genre = input("Enter the genre of the video game: ")
developer = input("Enter the developer: ")
classification = input("Enter the ESRB classification: ")

top_videogames.append({
    "name": name,
    "genre": genre,
    "developer": developer,
    "classification": classification
    })

while True:
    add_videogame = input("Do you want to add another videgame? (y/n) :")

    if add_videogame == "y":
        name = input("Enter the name of the video game: ")
        genre = input("Enter the genre of the video game: ")
        developer = input("Enter the developer: ")
        classification = input("Enter the ESRB classification: ")

        top_videogames.append({
        "name": name,
        "genre": genre,
        "developer": developer,
        "classification": classification
                })

    elif add_videogame == "n":
        print("Below you will find the videogames entred: ")
        break

    else:
        print("Enter a valid option (y/n)")


print (top_videogames)

videogames_csv('topvideogamestab.csv', top_videogames)
