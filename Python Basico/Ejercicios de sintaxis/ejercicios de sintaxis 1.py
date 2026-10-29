print("--- Welcome to price calculator ---")

discount02 = 0.2
discount01 = 0.1 


print("Enter the price of the product")
price = int (input("The price is: "))

final_discount2 = price * discount02
final_discount1 = price * discount01
final_price2 = price - final_discount2 
final_prince1 = price - final_discount1 


if price < 100:
    print (final_discount2)
    print (final_price2)
elif price > 100:
    print (final_discount1)
    print (final_prince1)
    




