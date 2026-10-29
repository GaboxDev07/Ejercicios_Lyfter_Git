lines(read_path)
    write_file_single_line(write_path,line)
    print(f"The above words have been sorted and save in the following file:", write_path)


main_sort_lines(
     input("Enter the file to be read: "),
     input("Enter the name of the new file: "))