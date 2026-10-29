print ("Bienvenido al ejercicio extra de excepciones 2")


def get_list():
    user_input = input ("Enter the numbers your want to convert to integer separated by ',': ")
    my_list = user_input.split(",")
    return my_list

def convert_to_int(my_list):
    for integer in my_list:
        try:
            converted_integer = int(integer)
            print (f"{integer}, has been converted to {converted_integer}")
        except ValueError:
            print (f"Could not convert the {integer}")
        


def main_converter():
    my_list = get_list()
    convert_to_int(my_list)

main_converter()
