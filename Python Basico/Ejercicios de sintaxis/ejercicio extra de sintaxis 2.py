print ("--- Try to find the hidden number ---")


print ("Enter 3 different numbers from 1 to 30")
number1 = int(input ("Enter the First number: "))
number2 = int(input ("Enter the Second number: "))
number3 = int(input ("Enter the Third number: "))

if number1 + number2 + number3 == 30 or number1 == 30 or number2 == 30 or number3 == 30:
    print ("Correct the you have entered the hidden number: 30")
else:
    print ("None of the numbers you entered matched the hidden number")

