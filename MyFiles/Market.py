# Make a market simulator

# Import required modules and libraries
import time
import random
import shutil

size = shutil.get_terminal_size().columns - 1
seps = "-" * size                  #Separators for better visibility of code
wait = [0.1, 0.2, 0.3, 0.4]     #wait as a variable to slow down the text and make it feel alive

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
        time.sleep(random.choice(wait))
        print(f"\n {seps} \n")
        print(f"Company name : {company}")
        print(f"Price of stock : {price}")
        print(f"Your money : {wallet}")
        print(f"Your shares : {share_held}")
        print(f"Stocks remaining : {stocks_available}")
        print(f"\n {seps} \n")

        #Make a variable that allows the user to control
        action = input(f"What would you like to do? (B)uy, (S)ell, (W)ait or (Q)uit. \n").strip().lower()
        time.sleep(random.choice(wait))
        if action in ("b", "1", "buy"):       #leave multiple options so if user type b or buy it works
            time.sleep(random.choice(wait))
            print("Purchase in progress ...")
            time.sleep(random.choice(wait))
            buy = int(input("How many shares you want to purchase? \n"))
            total_cost = buy * price
            if wallet >= total_cost and stocks_available >= buy:
                wallet -= total_cost
                share_held += buy
                stocks_available -= buy
                time.sleep(random.choice(wait))
                print("Succesfully bought the shares! \n")
            elif wallet < total_cost:
                time.sleep(random.choice(wait))
                print("You don't have enough money! \n")
            elif stocks_available < buy:
                time.sleep(random.choice(wait))
                print(f"{buy} are not available. Try selecting a lower amount. \n")
            else:                       #Create safety mechanism
                time.sleep(random.choice(wait))
                print("Error")
            time.sleep(random.choice(wait))
        elif action in ("s", "2", "sell"):
            time.sleep(random.choice(wait))
            print("Selling in progress ...")
            time.sleep(random.choice(wait))
            sell = int(input("How many shares you want to sell? \n"))
            total_profit = sell * price
            if share_held >= sell:
                wallet += total_profit
                share_held -= sell
                stocks_available += sell
                time.sleep(random.choice(wait))
                print("Succesfully sold the shares! \n")
            elif share_held < sell:
                time.sleep(random.choice(wait))
                print("You don't have enough shares! \n")
            else:                       #Create safety mechanism
                time.sleep(random.choice(wait))
                print("Error")
            time.sleep(random.choice(wait))
        elif action in ("w", "3", "wait"):
            time.sleep(random.choice(wait))
            print()
        elif action in ("q", "4", "quit"):
            time.sleep(random.choice(wait))
            confirmation = input("Are you sure you want to exit the simlation? \n")
            if confirmation in ("y", "yes"):
                time.sleep(random.choice(wait))
                print("Closed simulation")
                print(seps)
                simulating = False
            else:
                continue
            time.sleep(random.choice(wait))
        else:
            print("Error")      #make a safety mechanism

market()