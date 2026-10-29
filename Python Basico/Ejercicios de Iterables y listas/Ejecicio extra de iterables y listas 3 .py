print("Welcome to list and iterable extra practice 3")

my_list_of_numbers = []
lowest_number = 100


print ("Enter 10 numbers from 1 to 100")
for number in range(10):
    numbers = int(input("Enter the numbers now: "))
    my_list_of_numbers.append(numbers)

    if numbers < lowest_number:
        lowest_number = numbers

print ("The list of numbers entered was: ", my_list_of_numbers)
print ("The lowest number entered was: ", lowest_number)