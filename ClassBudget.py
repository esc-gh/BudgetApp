from os import name

# Function to prevent entry of non-integer or negative values. Avoid crashing the script
def non_neg(prompt):
    while True:
        try:
            user_input = int(input(prompt))
        except ValueError:
            print("Invalid input, please try again.")
            continue
        if user_input < 0:
            print("Input value cannot be negative, please try again.")
            continue
        else:
            break
    return user_input

# Main class for the app
class Budget:
    def __init__(self, balance, name):
        self.balance = balance
        self.name = name

    def __repr__(self):
        return

    def deposit(self, amount):
        self.balance=self.balance+amount
        return amount

    def withdraw(self, amount):
        self.balance=self.balance-amount
        return amount

    # Transfer function that works flexibly between any budget objects
    def transfer(self, destination):
        transfer = non_neg(f"Current {self.name} budget is £{self.balance} and {destination.name} budget is £{destination.balance}.\nEnter amount for transfer to {destination.name} budget (£): ")
        destination.deposit(self.withdraw(transfer))
        print(f"Transferred £{transfer}. New {destination.name} budget = £{destination.balance}")
    
    # Main method. The parameters allow flexible use of transfer method
    def function(self, c_budget, e_budget, f_budget):
        run_2 = True
        while run_2:
            run_3 = True
            while True:
                try:
                    control = int(input(f"{self.name} budget options - 1) Set new amount, 2) Deposit, 3) Withdraw, 4) Transfer or 5) Cancel: "))
                except ValueError:
                    print("Invalid input, please try again.")
                else:
                    break
            if control == 1:
                new_budget = non_neg(f"New {self.name} budget (£): ")
                self.balance = new_budget
            if control == 2:
                dpst = non_neg(f"Current {self.name} budget is £{self.balance}.\nDeposit amount (£): ")
                self.deposit(dpst)
            if control == 3:
                wdraw = non_neg(f"Current {self.name} budget is £{self.balance}.\nWithdrawal amount (£): ")
                self.withdraw(wdraw)
            if control == 4:
                while True:
                    if self.name == "Clothing":
                        trans = non_neg("Transfer to which budget? - 2) Entertainment or 3) Food: ")
                    if self.name == "Entertainment":
                        trans = non_neg("Transfer to which budget? - 1) Clothing or 3) Food: ")
                    if self.name == "Food":
                        trans = non_neg("Transfer to which budget? - 1) Clothing or 2) Entertainment: ")
                    if trans == 1 and self.name != "Clothing": # Conditional statement to prevent erroneous transfer from one budget back to itself
                        destination = c_budget
                        break
                    elif trans == 2 and self.name != "Entertainment":
                        destination = e_budget
                        break
                    elif trans == 3 and self.name != "Food":
                        destination = f_budget
                        break
                    else:
                        print("Invalid input, please try again.")
                self.transfer(destination)
            if control == 5:
                run_2 = False
                run_3 = False
            while run_3: # Runs at the end of any interaction other than 5/exit
                print(f"{self.name} Budget = £{self.balance}")
                cancel = str(input(f"Press C to continue editing {self.name}, or R to return to budget selection: ").upper())
                if cancel == "C" or cancel == "R":
                    run_3 = False
                if cancel == "R":
                    run_2 = False
                if cancel != "C" and cancel != "R":
                    print("Invalid input, please try again.")
