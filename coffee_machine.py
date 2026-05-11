'''
1 Penny = $0.01(1 cent)
1 nickel = $0.05(5 cent)
1 dimes = ).0.10(10 cent)
1 quarter = $0.25(25 cent)
espresso = $3.00
latte= $4.50
cappuccion = $6.00

'''

#initially
Milk_ML =750
Coffee_GM= 200
Water_ML=800
Money =0
def My_Coffee():
    global Milk_ML, Coffee_GM, Water_ML, Money
    req=input("What would you like to have (espresso/latte/cappuccino) ").lower()

    if req=="report":
        print("Total milk we have =",Milk_ML)
        print("Total coffee we have =",Coffee_GM)
        print("Total Water we have =",Water_ML)
        print("Total money we have is",Money)
        return 
    else:
        penny=float(input("How much penny you are inserting "))
        nickel=float(input("How much nickel you are inserting "))
        dimes=float(input("How much dimes you are inserting "))
        quarter=float(input("How much quarter you are inserting "))
        amount=penny*0.01+nickel*0.05+dimes*0.10+quarter*0.25

    if req=="espresso":
        if Milk_ML < 80 or Coffee_GM < 50 or Water_ML < 100:
            print("Sorry Resources are out of stock")
            print("Your Money has been refuned successfully")
        elif  amount < 3.00:
            print("You have not Inserted Sufficient money to place your order")
            print("Money Refunded successfully")
        else:
            Milk_ML-=80
            Coffee_GM-=50
            Water_ML-=100
            Money+=3.00
            print("Your espresso is ready...Enjoy Your Day")
            if amount > 3.00:
                print("The exchange of $",amount-3.00,"has been returned successfully")
    elif req=="latte":
        if Milk_ML < 100 or Coffee_GM < 70 or Water_ML < 130:
            print("Sorry Resources are out of stock")
            print("Your Money has been refuned successfully")
        elif amount < 4.50:
            print("You have not Inserted Sufficient money to place your order")
            print("Money Refunded successfully")
        else:
            Milk_ML-=100
            Coffee_GM-=70
            Water_ML-=130
            Money+=4.50
            print("Your latte is ready...Enjoy your day")
            if amount > 4.50:
                print("The exchange of $",amount-4.50,"has been returned successfully")
    elif req=="cappuccino":
        if Milk_ML <130 or Coffee_GM <80 or Water_ML < 150:
            print("Sorry Resources are out of stock")
            print("Your Money has been refuned successfully")
        elif amount < 6.00:
            print("You have not Inserted Sufficient money to place your order")
            print("Money Refunded successfully")
        else:
            Milk_ML-=130
            Coffee_GM-=80
            Water_ML-=150
            Money+=6.00
            print("Your cappuccino is ready...Enjoy your day")
            if amount > 6.00:
                print("The exchange of $",amount-6.00,"has been returned successfully")
ask="yes"
while ask=="yes":
    My_Coffee()
    ask=input("Type 'yes' to order your coffee....")

        