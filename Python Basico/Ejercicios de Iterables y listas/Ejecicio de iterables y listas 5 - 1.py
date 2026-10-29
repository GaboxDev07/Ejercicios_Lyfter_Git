print("Welcome to list and iterable practice 5")



print ("Enter 10 numbers from 1 to 100, separate by a space: ")
numbers = input("Enter the numbers now: ")

my_list_of_numbers = []

for number in numbers.split():
    my_list_of_numbers.append(int(number))


highest_number = my_list_of_numbers[0]
for number in my_list_of_numbers:
    if number > highest_number:
        highest_number = number
print(my_list_of_numbers)
print("The highest number was: ", highest_number)

