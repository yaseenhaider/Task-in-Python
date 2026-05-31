principal = float(input("Enter principal amount: "))

rate = float(input("Enter annual interest rate (%): "))

years = int(input("Enter number of years: "))


balance = principal
for year in range(1, years + 1):
    balance = balance * (1 + rate / 100)   
    print(f"Year {year}: Balance = {balance:.2f}")
