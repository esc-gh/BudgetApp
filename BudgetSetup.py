try:
    f = open("balance.txt","r")
    newuser = False
    f.close()
except IOError:
    newuser = True

if newuser == True:
    print("Welcome to Budget App! New user detected, please set up your starting budgets.")
    c_budget = int(input("New Clothing budget (£): "))
    e_budget = int(input("New Entertainment budget (£): "))
    f_budget = int(input("New Food budget (£): "))
    with open("balance.txt","w") as file:
        file.write(str(c_budget)+"\n")
        file.write(str(e_budget)+"\n")
        file.write(str(f_budget))
else:
    print("Welcome back to Budget App!")