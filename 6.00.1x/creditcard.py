monthly_interest = annualInterestRate / 12

for i in range(12):
    min_payment_monthly = monthlyPaymentRate * balance
    monthly_unpaid = balance - min_payment_monthly
    balance = monthly_unpaid + (monthly_interest * monthly_unpaid)
print('Remaining blalance: ', round(balance, 2))
