from ClassBudget import non-neg

# Check for presence of balance.txt file from scrpit being run previously
try:
    f = open("balance.txt","r")
    newuser = False
    f.close()
except IOError:
    newuser = True

# If the file doesn't exist then request starting values for budgets and save them
if newuser == True:
    print("Welcome to Budget App! New user detected, please set up your starting budgets.")
    c_budget = non-neg("New Clothing budget (£): "))
    e_budget = non-neg("New Entertainment budget (£): "))
    f_budget = non-neg("New Food budget (£): "))
    with open("balance.txt","w") as file:
        file.write(str(c_budget)+"\n")
        file.write(str(e_budget)+"\n")
        file.write(str(f_budget))
else:
    print("Welcome back to Budget App!")
