# Practice with numbers
salary = input("What's your monthly salary? ")
tax = input("How much tax you paying on salary? ")
bonusPercentage = input("What is percentage of monthly bonus? ")
bonus = float(bonusPercentage)/100 * int(salary)
print("Your monthly bonus is " + str(bonus))
grossSalary = int(salary) - int(tax) + float(bonus)

print("Your total salary is: " + str(grossSalary))