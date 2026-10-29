print("Welcome to list and iterable practice 4")

list_of_numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]
even_numbers = []

for even in range(len(list_of_numbers)):
    if list_of_numbers [even] % 2 == 0:
        even_numbers.append(list_of_numbers[even])
print(even_numbers)