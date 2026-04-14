# Make a market simulator

# Import required modules and libraries
import random

seps = "-"*100                  #Separators for better visibility of code

#Define a function to run the simulation
def market():

    # Make required variables
    company = random.choice(["Mango-Slop", "Pear", "Stone", "Titan", "Tech-Slop"])      #Name of the company
    price = 100.00              #Price of each stock
    wallet = 1000.00            #Money you have
    share_held = 0              #No. if shares u have
    stocks_available = 1000     #No. of stocks available

    # Make a loop that shows the user its staus before making any changes
    simulating = True
    while simulating == True:
        print(f"\n {seps} \n")
        print(f"Company name : {company}")
        print(f"Price of stock : {price}")
        print(f"Your money : {wallet}")
        print(f"Your shares : {share_held}")
        print(f"Stocks remaining : {stocks_available}")
        print(f"\n {seps} \n")

        #Make a variable that allows the user to control
        action = input(f"What would you like to do? (B)uy, (S)ell, (W)ait or (Q)uit. \n").strip().lower()
        if action in ("b", "1", "buy"):       #leave multiple options so if user type b or buy it works
            print("Purchase in progress ...")
            buy = int(input("How many shares you want to purchase? \n"))
            total_cost = buy * price
            if wallet >= total_cost and stocks_available >= buy:
                wallet -= total_cost
                share_held += buy
                stocks_available -= buy
                print("Succesfully bought the shares \n")
            elif wallet < total_cost:
                print("You don't have enough money /n")
            elif stocks_available < buy:
                print(f"{buy} are not available. Try selecting a lower amount. \n")
            else:                       #Create safety mechanism
                print("Error")
            
        elif action in ("s", "2", "sell"):
            print()
        elif action in ("w", "3", "wait"):
            print()
        elif action in ("q", "4", "quit"):
            confirmation = input("Are you sure you want to exit the simlation? \n")
            if confirmation in ("y", "yes"):
                print("Closed simulation")
                simulating = False
            else:
                continue
        else:
            print("Error")      #make a safety mechanism

market()