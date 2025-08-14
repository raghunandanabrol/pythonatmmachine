balance = 1000

print("""
Welcome to ATM Machine

Choose Transaction

1) BALANCE
2) WITHDRAW
3) DEPOSIT
4) EXIT
""")

option = int(input("Enter Transaction: "))

if option == 1:
    print("Your balance is:", balance)

elif option == 2:
    withdraw = float(input("Enter amount to withdraw: "))
    if balance >= withdraw:
        balance -= withdraw
        print("Success")
        print("Your new balance is:", balance)
    else:
        print("Insufficient balance")

elif option == 3:
    deposit = float(input("Enter amount to deposit: "))
    balance += deposit
    print("Success")
    print("Total balance now is:", balance)

elif option == 4:
    print("Thank you for using our ATM!")
    exit()

else:
    print("No valid transaction selected")
