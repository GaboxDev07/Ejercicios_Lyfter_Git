


def append_to_file(write_path,line):
    with open(write_path, 'a', encoding='utf-8') as file:
           file.write(line + "\n")


def main_append_line(write_path,line):
        print ("Bienvenido a ejercicio extra de manejor de archivos 4")
        append_to_file(write_path,line)
        print("The text has been appended to the file.")


main_append_line(
      input("Enter the name of the file: "),
      input("Please enter the text for the file to store it: ")
)
