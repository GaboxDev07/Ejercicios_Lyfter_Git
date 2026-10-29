print ("Bienvenido al ejercicio extra de excepciones 3")


def get_list():
    user_input = input ("Enter the numbers, floats or strings your want to convert to integer separated by ',': ")
    my_list = user_input.split(",")
    return my_list

def convert_to_float(my_list):
    for element in my_list:
        try:
            converted_float = float(element)
            print (f"{element}, has been converted to {converted_float}")
        except ValueError:
            print (f"{element}")


def sum_of_elements(my_list):
    total = 0

    for element in my_list:
            try:
                converted_float = float(element)
                total = converted_float + total
                print(f"The sum was done correctly {converted_float}")
            except ValueError:
                print (f"Invalid element: {element}")
    print(total) 


def main_converter():
    my_list = get_list()
    convert_to_float(my_list)
    sum_of_elements(my_list)


main_converter()