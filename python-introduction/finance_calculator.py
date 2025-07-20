
monthly_income = float(input("Enter your monthly income: "))
monthly_expenses = float(input("Enter your total monthly expenses: "))

monthly_savings = monthly_income - monthly_expenses

annual_savings = monthly_savings * 12
INTEREST_RATE = 0.05
projected_annual_savings = annual_savings + (annual_savings * INTEREST_RATE)

print(f"Your monthly savings: ${monthly_savings:.2f}")
print(
    f"Your projected annual savings (with 5% interest): ${projected_annual_savings:.2f}")
