import random
import time

OPERATORS = ['+', '-', '*']
MIN_OPERAND = 3
MAX_OPERAND = 12
TOTAL_CHALLENGES = 10


def generate_challenge():
    left = random.randint(MIN_OPERAND, MAX_OPERAND)
    right = random.randint(MIN_OPERAND, MAX_OPERAND)
    operator = random.choice(OPERATORS)

    expression = f'{left} {operator} {right}'
    answer = eval(expression)
    return expression, answer


wrong = 0
correct = 0
input('Press enter to start!')
print('-------------------------------------------------------')
start_time = time.time()


for index in range(TOTAL_CHALLENGES):
    challenge, answer = generate_challenge()
    while True:
        guess = input(f'Problem #{index+1}: {challenge} = ')
        if guess == str(answer):
            correct += 1
            break
        wrong += 1

end_time = time.time()
time_taken = end_time-start_time

print('-------------------------------------------------------')
print('Well done! You finished in ', round(time_taken, 2), 'seconds!')
print(f'You got ', correct, 'out of', TOTAL_CHALLENGES)
