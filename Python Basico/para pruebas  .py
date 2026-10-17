add_videogame = input("Do you want to add another videgame? (y/n) :")

while add_videogame == "y":
    try:
        add_videogame = input("Do you want to add another videgame? (y/n) :")
        if add_videogame == "n":

    name = input("Enter the name of the video game: ")
    genre = input("Enter the genre of the video game: ")
    developer = input("Enter the developer: ")
    classification = input("Enter the ESRB classification: ")
    else:
        print(f"Invalid input, please enter a valid name, genre, dev or class")
    except NameError:
            print(f"Invalid input, please enter a valid name, genre, dev or class")

        


    top_videogames.append({
        "name": name,
        "genre": genre,
        "developer": developer,
        "classification": classification
        })

    add_videogame = input("Do you want to add another videgame? (y/n) :")