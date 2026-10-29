print("Welcome to list and iterable extra practice 4")

my_list_of_numbers = []
total_numbers = 5
total = 0
above_average_numbers_list = []


print ("Enter 5 numbers from 1 to 100")
for number in range(5):
    numbers = int(input("Enter the numbers now: "))
    my_list_of_numbers.append(numbers)
    total = total + numbers

average_number = total / total_numbers

for above_average in my_list_of_numbers:
    if above_average > average_number:
        above_average_numbers_list.append(above_average)


print (my_list_of_numbers)
print (total)
print (average_number)
print (above_average_numbers_list)

