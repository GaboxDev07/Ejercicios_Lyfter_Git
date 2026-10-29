import os

print(os.getcwd())
print("looking for the file in: ")



def read_file_by_lines(read_path):
    with open(read_path, 'r', encoding='utf-8') as file:
        lines = file.readlines()
        for number, line in enumerate(lines, start=1):
            print(f"Line {number}: {line.strip()}")

        return(lines)

def write_sorted_names(write_path,text):
    with open(write_path, 'w', encoding='utf-8') as file:
        text.sort()
        for name in text:
            file.write(name)



def main_sort_text(read_path,write_path):
    print("Welcome to the Ejecicio de Manejo De archivos 1")
    names = read_file_by_lines(read_path)
    write_sorted_names(write_path,names)
    print(f"The above names have been sorted and save in the following file: new_sorted_list.txt" )

main_sort_text('songs_name.txt','new_sorted_list.txt')