from helper import reset
from game import play_game, player_input

if __name__ == "__main__":
    play_again = True
    player_1, player_2 = player_input()

    while play_again:
        i, sample, valid = reset()
        play_game(i, valid, sample, player_1, player_2)
        replay_decide = input('Do you want to play again? Choose Y or N: ')
        play_again = replay_decide.upper() == 'Y'
    pass
