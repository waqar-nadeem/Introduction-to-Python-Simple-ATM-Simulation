balance = 1000
while True:
    print("1.Deposit 2.Withdraw 3.Balance 4.Exit")
    c = input("Choose: ")
    if c == "1":
        amt = int(input("Amount: "))
        balance += amt
    elif c == "2":
        amt = int(input("Amount: "))
        if amt <= balance:
            balance -= amt
        else:
            print("Insufficient funds")
    elif c == "3":
        print("Balance:", balance)
    elif c == "4":
        break
