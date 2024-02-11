import random

user_number = input('Type a number: ')
if user_number.isdigit():
    user_number = int(user_number)
    if user_number <= 0:
        print('Please enter a number greater than 0 to continue')
        quit()
else:
    print('Please type a number to continue')
    quit()
randon_number = random.randint(0, user_number)
user_guesses = 0
while True:
    user_guesses += 1
    user_guess = input('Make a guess: ')
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print('Please type a number to continue')
        continue
    if user_guess == randon_number:
        print('You got it correct!')
        break
    elif user_guess > randon_number:
        print('You were above the number')
    else:
        print('You were below the number')

print(f'You got it in {user_guesses} guesses!')
