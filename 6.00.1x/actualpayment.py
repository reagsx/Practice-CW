balance = 3329
annualInterestRate = .2
months = 12
monthly_interest = annualInterestRate / 12


discount = (((1 + monthly_interest) ** months) - 1) /\
           (monthly_interest * (1 + monthly_interest) ** months)

payment = balance / discount


print(payment)
