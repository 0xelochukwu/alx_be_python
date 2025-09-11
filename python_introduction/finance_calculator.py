monthly_income = int(input("Enter your monthly income: "))
monthly_expenses = int(input("Enter your monthly expenses: "))

monthly_savings = float(monthly_income) - float(monthly_expenses)

projected_savings = int(monthly_savings * 12 + (monthly_savings * 12 * 0.05))

print("Enter your monthly income: " + str(monthly_income))
print("Enter your total monthly expenses: " + str(monthly_expenses))
print("Your monthly savings are $"+str(monthly_savings))
print("Projected savings after one year, with interest, is: $"+str(projected_savings))