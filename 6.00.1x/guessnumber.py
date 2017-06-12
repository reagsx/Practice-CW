# Gather inputs, test high and low
print("Please enter number 0 - 99:")

high = 100
low = 0
v = ''

while v != 'c':
    guess = (high+low) // 2
    print('Is your number:', guess, '?')
    v = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly. ")
    if v == 'h':
        high = guess
    elif v == 'l':
        low = guess
    elif v == 'c':
        #score!
        v = 'c'
    else:
        v = input("Input not understood, please re-enter 'h' for too high, 'l' for too low, or 'c' if I guessed correctly. ")

print('Game over! Your secret number was: ' + str(guess))
