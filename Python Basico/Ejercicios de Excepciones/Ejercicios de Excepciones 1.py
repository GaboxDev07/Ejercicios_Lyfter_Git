print ("Welcome to the Ejercicio extra de Excepciones 1")

def show_menu():
    print("Select one of the following options: ")
    print("1 to add (+)")
    print("2 to subtract (-)") 
    print("3 to multiply (x) ")
    print("4 to divide (÷)")
    print("5 to clear result ")
    print("6 to exit")


def option_selection():
    while True:
        try:
            selected_option = int(input("Please enter the selected option: "))
            if selected_option >= 1 and selected_option <= 6:
                return(selected_option)
            else:
                print(f"Invalid option. Please enter a valid option from 1 to 6.")
        except ValueError:
            print(f"Invalid option. Please enter a valid option from 1 to 6. ")
        

def get_number():
    while True:
        try:
            entered_number = int(input("Please enter a number: "))
            break
        except ValueError:
            print(f"There was an error while entering the number")
    return entered_number

def add(current_number,entered_number):
    total = current_number + entered_number
    return(total)


def subtract(current_number,entered_number):
    total = current_number - entered_number
    return(total)


def multiply(current_number,entered_number):
    total = current_number * entered_number
    return(total)


def divide(current_number,entered_number):
    while True:
        try:
            total = current_number / entered_number
            return(total)
        except ZeroDivisionError:
            print(f"You Cannot divide by zero. Please enter a number other than 0 ")
            entered_number = get_number()


def main_calculator():
    current_number = 10
    while True:
        show_menu()
        selected_option = option_selection()

        if selected_option == 1:
            entered_number = get_number()
            current_number = add(current_number,entered_number)
            print(current_number)

        elif selected_option == 2:
            entered_number = get_number()
            current_number = subtract(current_number,entered_number)
            print(current_number)

        elif selected_option == 3:
            entered_number = get_number()
            current_number = multiply(current_number,entered_number)
            print(current_number)

        elif selected_option == 4:
            entered_number = get_number()
            current_number = divide(current_number,entered_number)
            print(current_number)

        elif selected_option == 5:
            current_number = 10
            print(current_number)

        elif selected_option == 6:
            break

main_calculator()




