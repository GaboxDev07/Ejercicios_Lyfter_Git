print("--- Welcome Mutliplication tables---")

counter = 0
number  = int (input("Enter a number from 1 to 10: "))

while number < 1 or number > 10:
    print ("Please enter a number between 1 and 10.")
    number  = int (input("Enter a number from 1 to 10: "))
while counter <=11:
    counter = counter + 1
    result = (number * counter)
    print (number, "X", counter, "=", result)
    




