print('Welcome to our quiz game!')

playing = input('Do you want to play? ')

if playing.lower() != 'yes':
    quit()
print('Alright. Lets begin!')

score = 0

answer = input('What does RAM stand for? ')
if answer.lower() == 'random access memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')
answer = input('What does ROM stand for? ')
if answer.lower() == 'read only memory':
    print('Correct!')
    score += 1
else:
    print('Incorrect!')

print(f'You got {score} question(s) correct!')
print(f'Your score is {(score/2)*100}%')
