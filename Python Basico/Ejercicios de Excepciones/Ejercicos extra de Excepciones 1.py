print("Bienvenido al ejercicio extra de exepciones 1")


def get_name():
    while True:
        try:
            name = input("Please enter your name: ")
            if name.isdigit():
                raise ValueError("There was and error, name cannot be a number")
    
            return name
        except ValueError as error:
            print(error)


def get_age():
    while True:
        try:
            age = int(input("Please enter your age: "))
            break
        except ValueError:
            print(f"There was an error while entering the number")
    return age


def main_user_data():
    name = get_name()
    age = get_age()
    print (f"Hi {name}, your age is {age}")


main_user_data()