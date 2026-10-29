print ("Bienvenido a ejercicio extra de manejor de archivos 2")

def read_file_by_lines(read_path):
    content = []
    with open(read_path, 'r', encoding='utf-8') as file:
        for words in file:
            words = words.split()
            content.extend(words)
        return content

def count_words(content):
    counter = 0
    for words in content:
        counter += 1
    return counter

def write_counted_words(write_path,counter):
    with open(write_path, 'w', encoding='utf-8') as file:
        file.write(f"This file contains {counter} words")


def main_total_words(read_path,write_path):
    print ("Bienvenido a ejercicio extra de manejor de archivos 2")
    content = read_file_by_lines(read_path)
    counter = count_words(content)
    write_counted_words(write_path,counter)
    print((f"This file contains {counter} words"))


main_total_words(
    input("Enter the file to be read: "),
    input("Enter the name of the new file: ")
)


