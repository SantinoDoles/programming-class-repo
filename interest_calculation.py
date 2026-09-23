investment_amount = int(input("Enter the monthly investment amount: "))
while investment_amount <= 0 or investment_amount >= 50000:
    print("Invalid investment amount. Please try again.")
    investment_amount = int(input("Enter the monthly investment amount: "))
interest_rate = int(input("Enter the yearly interest rate: "))
while interest_rate <= 0 or interest_rate >= 15:
    print("Invalid interest rate. Please try again.")
    interest_rate = int(input("Enter the yearly interest rate: "))
investment_years = int(input("Enter the investment duration in years: "))
while investment_years <= 0:
    print("Invalid investment duration. Please try again.")
    investment_years = int(input("Enter the investment duration in years: "))
total_months = investment_years * 12
monthly_interest_rate = interest_rate / 12 / 100
total = 0
for month in range(1, total_months + 1):
    total = total + investment_amount
    interest = round(total * monthly_interest_rate, 2)
    total = total + interest
    if month % 12 == 0:
        current_year = month // 12
        print("Year", current_year, "Investment Value: $", round(total, 2))
print("Years:", investment_years)
print("Yearly Interest Rate:", interest_rate, "%")
print("Monthly Investment Amount: $", investment_amount)
print("Final Investment Amount: $", round(total, 2))
print("Completed by Santino Doles")

