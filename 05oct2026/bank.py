balance = int(input("enter the balance:"))
amount = int(input("enter the amount:"))
if amount<=balance and amount %500==0:
    print("allow withdraw")
else:
    print("not allowed")
      