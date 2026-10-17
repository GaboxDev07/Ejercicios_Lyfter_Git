import csv


print("Bienvenidos al ejercicio de manejo de csvs 2")


def videogames_csv(write_path, data):
    with open(write_path,'w', encoding='utf-8', newline='' ) as file:
        headers = data[0].keys()

        writer = csv.DictWriter(file, fieldnames=headers, delimiter = '\t')
        writer.writeheader()
        writer.writerows(data)

def get_number_of_videogames():
    number_of_videogames = int (input("How many videogames you want to enter ?: "))
    return number_of_videogames
    
    

def get_videogames_data(number_of_videogames):

    top_videogames = []

    

    for number in range(number_of_videogames):
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

    return top_videogames

number_of_videogames = get_number_of_videogames()

top_videogames = get_videogames_data(number_of_videogames)

print (top_videogames)

videogames_csv('topvideogamestab.csv', top_videogames)
