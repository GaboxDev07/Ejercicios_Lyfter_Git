print("Welcome to list and iterable practice 5")

print ("Enter 10 numbers from 1 to 100")


my_list_of_numbers = []
highest_number = 0

for number in range (2):
    numbers = int(input("Enter the numbers now: "))
    my_list_of_numbers.append(numbers)

    if numbers > highest_number:
        highest_number = numbers

print ("The list of numbers entered was: ", my_list_of_numbers)
print ("The highest number entered was: ", highest_number)



