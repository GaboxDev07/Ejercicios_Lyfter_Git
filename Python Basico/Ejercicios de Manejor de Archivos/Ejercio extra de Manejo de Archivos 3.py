

def read_file_by_lines(read_path):
     upper_words = []
     with open(read_path, 'r', encoding='utf-8') as file:
            for words in file:
                upper_words.append(words.upper())
            return upper_words


def write_uppercase_lines(write_path, upper_words):
     with open(write_path, 'w', encoding='utf-8') as file:
          for words in upper_words:
            file.write(words)
            


def main_uppercase_file(read_path, write_path):
    print ("Bienvenido a ejercicio extra de manejor de archivos 3")
    upper_words = read_file_by_lines(read_path)
    words_capitalized = write_uppercase_lines(write_path,upper_words)
    print("All the letters has been capitalized") 

main_uppercase_file(
     input("Enter the file to be capitalized: "),
     input("Give a name to the new file: ")
)
