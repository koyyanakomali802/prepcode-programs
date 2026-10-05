price1 = int(input("enter the price1:"))
price2 = int(input("enter the price2:"))
if price1 < price2:
    print("first product is cheaper")
elif price1 > price2:
    print("second product is more expensive")
else:
    print("two products are the same price")