amount_due = 50

while amount_due >0:
    print("Amount Due: ", amount_due)
    coin = int(input("Insert Coin: "))
    if coin in [25, 10,5]:
        amount_due -= coin
if amount_due < 0:
    change_owed = int(amount_due)*(-1)
    print("Change Owed: ",change_owed)


