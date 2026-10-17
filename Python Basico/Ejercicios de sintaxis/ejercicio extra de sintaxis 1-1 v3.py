print("--- Welcome to price calculator ---")

discount01 = 0.1 
discount02 = 0.02

print("Enter the price of the product")
price = float (input("The price is: "))

#Discount of 10%
final_discount1 = price * discount01
final_price1 = price - final_discount1

#Discount of 2%
final_discount2 = price * discount02
final_price2 = price - final_discount2



if price < 100:
    print ("Discount: ", final_discount2)
    print ("Final price with discount applied:", final_price2)
elif price >= 100:
    print ("Discount: ", final_discount1)
    print ("Final price with discount applied:",final_price1)
    




