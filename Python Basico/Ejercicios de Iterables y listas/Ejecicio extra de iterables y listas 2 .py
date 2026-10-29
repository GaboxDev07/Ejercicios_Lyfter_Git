print("Welcome to list and iterable extra practice 2")

my_list_of_numbers = []
negative = False

print ("Enter 10 numbers from 1 to 100, can be positive + or negative - : ")
for number in range (10):
    number = int(input("Enter the numbers now: "))
    my_list_of_numbers.append(number)

    if number <=0:
        negative = True

if negative == True:
        print ("You enter at least one negative number")
else:
        print ("All the numbers are positive.")

print(my_list_of_numbers)