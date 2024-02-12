from curses.ascii import isdigit
import random


def roll_dice():
    minimum_value = 1
    maximum_value = 6
    roll = random.randint(minimum_value, maximum_value)

    return roll


while True:
    number_of_players = input('Enter number of players (2-4) ').lower()

    if number_of_players.isdigit():
        number_of_players = int(number_of_players)
        if 2 <= number_of_players <= 5:
            break
        else:
            print('Must be between 2-4 players')
    else:
        print('Invalid number. Try again')

maximum_score = 50
player_scores = [0 for _ in range(number_of_players)]

while max(player_scores) < maximum_score:
    for player_index in range(number_of_players):
        print('\nPlayer number ', player_index+1, 'turn has just started\n')
        print('Your total score is: ', player_scores[player_index], '\n')
        current_player_score = 0
        while True:
            can_roll = input(
                'Would you like to roll?. Type y for yes: ').lower()
            if can_roll != 'y':
                break
            value = roll_dice()
            print(value)
            if value == 1:
                print('You rolled a 1! Turn done!')
                current_player_score = 0
                break
            else:
                print('You rolled a:', value)
                current_player_score += value
            print('Your score is: ', current_player_score)

        player_scores[player_index] += current_player_score
        print('Your total score is:', player_scores[player_index])

maximum_score = max(player_scores)
winner = player_scores.index(maximum_score)
print('Player ', winner+1, 'is the winner with a score of:', maximum_score)
