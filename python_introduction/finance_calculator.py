monthlyIncome = int(input("Enter your monthly income: "))
monthlyExpenses = int(input("Enter your monthly expenses: "))

monthlySavings = float(monthlyIncome) - float(monthlyExpenses)

projectedSavings = int(monthlySavings * 12 + (monthlySavings * 12 * 0.05))

print("Enter your monthly income: " + str(monthlyIncome))
print("Enter your total monthly expenses: " + str(monthlyExpenses))
print("Your monthly savings are $"+str(monthlySavings))
print("Projected savings after one year, with interest, is: $"+str(projectedSavings))