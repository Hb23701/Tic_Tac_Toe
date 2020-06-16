from helper import display_board

#take input from player 1 and 2 on their markers
def player_input():
    marker = ''
    while marker != 'x' and marker != 'o':
        marker = input('Player 1, choose either x or o: ')
        
    player_1 = marker
    if player_1 == 'x':
            player_2 = 'o'
    else:
        player_2 = 'x'
        
    return (player_1, player_2)


def play_game(i, valid, sample, player_1, player_2):
    while ' ' in sample[1:]:
        if i%2 == 0:
            player = player_1
        else:
            player = player_2
        if valid:
            a = 'which'
        else:
            a = 'another'
        choose_position = int(input(f'Board starts from bottom left corner. choose {a} position you want to put {player} in (1-9): '))
        valid = choose_position > 0 and choose_position < 10 and sample[choose_position] == ' '

        if valid:
            sample[choose_position] = player
            display_board(sample)
            i+=1

        if sample[1] == sample [2] == sample [3] == player:
            print (f'{player} won')
            break
        elif sample[4] == sample [5] == sample [6] == player:
            print (f'{player} won')
            break
        elif sample[7] == sample [8] == sample [9] == player:
            print (f'{player} won')
            break
        elif sample[1] == sample [4] == sample [7] == player:
            print (f'{player} won')
            break
        elif sample[2] == sample [5] == sample [8] == player:
            print (f'{player} won')
            break
        elif sample[3] == sample [6] == sample [9] == player:
            print (f'{player} won')
            break
        elif sample[3] == sample [5] == sample [7] == player:
            print (f'{player} won')
            break
        elif sample[1] == sample [5] == sample [9] == player:
            print (f'{player} won')
            break
        elif ' ' not in sample[1:]:
            print ("It's a tie")
