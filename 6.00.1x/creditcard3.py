# Given Variables
balance = 320000
annualInterestRate = 0.2

# My Variables
monthly_interest = annualInterestRate / 12
lower = balance / 12
upper = (balance * (1 + monthly_interest) ** 12) / 12
payment = (upper + lower) / 2
epsilon = .01


# Calculate Here While Loop is Broken, need to include interest
while True:
    print(payment, upper, lower)
    nb = balance

    for i in range(12):
        nb = (nb - payment) * (1 + monthly_interest)
    print(nb)
    if nb < 0:
        upper = payment
    elif nb > 0:
        lower = payment
    elif nb - balance >= epsilon:
        break

    payment = (upper + lower) / 2

print(round(payment, 2))
