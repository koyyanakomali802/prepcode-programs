buying_price = int(input("enter the buying price:"))
selling_price = int(input("enter the selling price:"))
total_products = int(input("enter the amount of products:"))
storage_price = int(input("enter the storage amount:"))

profit = ((buying_price - selling_price) * total_products - storage_price)
print(f"total profits = {profit}")