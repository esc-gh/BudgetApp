from ClassBudget import Budget, non_neg
# Check for new user or existing data
import BudgetSetup

# Load data from pevious session or which has just been added via BudgetSetup
with open("balance.txt","r") as file:
    var = file.readlines()

c_budget = Budget(int(var[0]), "Clothing")
e_budget = Budget(int(var[1]), "Entertainment")
f_budget = Budget(int(var[2]), "Food")

# Main loop
run=True
while run:
    control = str(input("~~ To see a Budget Summary, press S. To Exit press X.\nOr select a Budget - 1) Clothing, 2) Enterntainment, 3) Food: ").upper())
    if control == "1":
        c_budget.function(c_budget, e_budget, f_budget)
    elif control == "2":
        e_budget.function(c_budget, e_budget, f_budget)
    elif control == "3":
        f_budget.function(c_budget, e_budget, f_budget)
    elif control == "X":
        run = False
    elif control == "S": # Budget breakdown with category totals and percentages
        total_budget=(c_budget.balance,e_budget.balance,f_budget.balance)
        per_c = c_budget.balance/sum(total_budget)
        per_e = e_budget.balance/sum(total_budget)
        per_f = f_budget.balance/sum(total_budget)
        print(f"Your total budget is currently £{sum(total_budget)}.\nBreakdown by category:\n\tClothing\t= {c_budget.balance} - {per_c:.2%}\n\tEntertainment\t= {e_budget.balance} - {per_e:.2%}\n\tFood\t\t= {f_budget.balance} - {per_f:.2%}")
        input("Press any key to return to start: ")
    else:
        print("Invalid input, please try again.")

# Closing section with budget summary and confirmation of whether to save to balance.txt file before exiting
total_budget=(c_budget.balance,e_budget.balance,f_budget.balance)
print(f"Budget breakdown: Clothing = £{c_budget.balance}, Entertainment = £{e_budget.balance}, Food = £{f_budget.balance}")
print(f"Your total budget remaining = £{sum(total_budget)}")
run_4 = True
while run_4:
    end=str(input("Would you like to save changes before quitting? (Y/N): ").upper())
    if end == "Y":
        confirm = str(input("Confirm you want to save? (Y/N): ").upper())
        if confirm == "Y":
            with open("balance.txt","w") as file:
                file.write(str(c_budget.balance)+"\n")
                file.write(str(e_budget.balance)+"\n")
                file.write(str(f_budget.balance))
            print("Changes saved - Thanks for using Budget App!")
            run_4 = False
        if confirm != "N" and confirm != "Y":
            print("Invalid input.")
    if end == "N":
        confirm = str(input("Quitting without saving, are you sure? (Y/N): ").upper())
        if confirm == "Y":
            print("Good Bye!")
            run_4 = False
        if confirm != "N" and confirm != "Y":
            print("Invalid input.")
