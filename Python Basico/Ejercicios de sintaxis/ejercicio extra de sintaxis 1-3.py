print ("--- Welcome to the total sum of the number you enter ---")


counter = 1
total_sum = 0 


number = int(input("Ingrese un numero cualquiera: "))

while counter <= number:
    total_sum = total_sum + counter
    counter = counter + 1 
print ("The total sum of the numbers  from 1 to", number,"is", total_sum)

