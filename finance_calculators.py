import math
calculator = input("""Choose either 'investment' or 'bond' from the menu below to proceed:

investment - to calculate the amount of interest you'll earn on your investment
bond - to calculate the amount you'll have to pay on a home loan
""") 

if calculator == "investment" or calculator == "Investment" or calculator == "INVESTMENT":
    deposit = float(input("How much money are you depositing? £"))
    interest_rate = float(input("What is the interest rate? "))
    years = int(input("How many years do you plan on investing this money for? "))
    interest = input("Would you like simple or compounding interest? ")
    
    if interest == "simple" or interest == "Simple" or interest == "SIMPLE":
        print(f"You would have £{round(deposit * (1 + (interest_rate / 100) * years))} after {years} years.")
    elif interest == "compounding" or interest == "Compounding" or interest == "COMPOUNDING":
        print(f"You would have £{round(deposit * math.pow((1 + (interest_rate / 100)), years))} after {years} years.")
    else:
        print("I'm sorry, I do not recognise that answer. You may have mispelled it.")

elif calculator == "bond" or calculator == "Bond" or calculator == "BOND":
    value = int(input("What is the present value of the house? £"))
    bond_interest_rate = int(input("What is the interest rate? "))
    months = int(input("Over how many months do you plan to repay? "))

    #must divide the interest rate by 100 to get it as a decimal
    monthly_interest = (bond_interest_rate / 100 / 12)

    #round to 2 decimals as it is currency
    #** means to the power of and is cleaner
    print(f"Your monthly repayments will be £{round((monthly_interest * value)/(1 - (1 + monthly_interest)**(- months)), 2)}.")

elif len(calculator) == 0:
    print("Please enter 'investment' or 'bond'.")

else:
    print("I'm sorry, I do not recognise that answer. You may have mispelled it.")