import random

print('Hello!')
print("Let's play!")
computer_number = random.randint(1, 100)
flag = False
count_player_inputs = 0
record_inputs = 4
while True:
    player_input = input('Guess the number between 1 and 100:')
    if not player_input.isdigit():
        print('Invalid input. Try again.')
        continue
    player_number = int(player_input)
    count_player_inputs += 1
    if player_number == computer_number:
        print('Great job! You guess it!')
        if count_player_inputs < record_inputs:
            print(f'Your broke the record! You guess it with only {count_player_inputs} try/ies!')
        else:
            print(f'You made {count_player_inputs} tries. The record is still not broken!')
            print('Wanna break the record?')
            count_player_inputs = 0
            flag = True
            break
    elif player_number > computer_number:
        print('You are aiming too high!')
    else:
        print('You are aiming too low!')

if flag:
    new_game = input('Type [yes] to play or [no] to quit:')
    while new_game == 'yes':
        player_input = input('Guess the number between 1 and 100:')
        if not player_input.isdigit():
            print('Invalid input. Try again.')
            continue
        player_number = int(player_input)
        count_player_inputs += 1
        if player_number == computer_number:
            print('Great job! You guess it!')
            if count_player_inputs < record_inputs:
                print(f'Your broke the record! You guess it with only {count_player_inputs} try/ies!')
            else:
                print(f'You made {count_player_inputs} tries. The record is still not broken!')
                print('Wanna break the record?')
                flag = True
                break
        elif player_number > computer_number:
            print('You are aiming too high!')
        else:
            print('You are aiming too low!')
    new_game = input('Type [yes] to play or [no] to quit:')


