
import os
print("Current working directory:", os.getcwd())
print("Python script location:", os.path.dirname(os.path.abspath(__file__)))

def read_file_by_lines(read_path):
    content = " "
    with open(read_path, 'r', encoding='utf-8') as file:
        for line in file:
            clean_line = line.replace("\n", " ")
            content += clean_line
    return content

def write_file_single_line(write_path,line):
    with open(write_path, 'w', encoding='utf-8') as file:
            file.write(line)


def main_sort_lines(read_path,write_path):
    print ("Bienvenido a ejercicio extra de manejor de archivos 1")
    line = read_file_by_lines(read_path)
    write_file_single_line(write_path,line)
    print(f"The above words have been sorted and save in the following file:", write_path)


main_sort_lines(
     input("Enter the file to be read: "),
     input("Enter the name of the new file: "))