# Given Variables
balance = 3329
annualInterestRate = .2
payment = 0

# My Variables
monthly_interest = annualInterestRate / 12
payment = 0

# Calculate Here
while True:
    end_balance = balance
    payment += 10
    for i in range(12):
        monthly_unpaid = end_balance - payment
        end_balance = monthly_unpaid + (monthly_interest * monthly_unpaid)
    if end_balance <= 0:
        break

print(payment)
