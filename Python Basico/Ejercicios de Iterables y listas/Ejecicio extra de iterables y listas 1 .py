print("Welcome to list and iterable extra practice 1")

print ("Enter 10 numbers from 1 to 100, separate by a space: ")
numbers = input("Enter the numbers now: ")

my_list_of_numbers = []
counter = 0

searched_number = int(input("Enter the number you want to search: "))
for number in numbers.split():
    number = int(number)
    my_list_of_numbers.append(number)
    if searched_number == number:
        counter += 1

if counter == 0:
    print ("The number you are looking for was not entered.")
else:
    print ("The number you are searching", searched_number, "shows up : ", counter, "veces")

