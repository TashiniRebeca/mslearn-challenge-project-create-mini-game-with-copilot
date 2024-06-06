#Creating a rock, paper, scissor game using python
#The player can choose one of the three options rock, paper, or scissors and should be warned if they enter an invalid option.
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
#By the end of each round, the player can choose whether to play again.
#Display the player's score at the end of the game.
#The minigame must handle user inputs, putting them in lowercase and informing the user if the option is invalid.

import random
#The game must be played against the computer.
#The computer must randomly choose one of the three options.

def computer_choice():
    options = ['rock', 'paper', 'scissors']
    return random.choice(options)

#The player must choose one of the three options.
def player_choice():
    player = input('Choose rock, paper, or scissors: ')
    player = player.lower()
    if player in ['rock', 'paper', 'scissors']:
        return player
    else:
        print('Invalid option. Try again.')
        return player_choice()
    
#At each round, the player must enter one of the options in the list and be informed if they won, lost, or tied with the opponent.
def play_round():
    player = player_choice()
    computer = computer_choice()
    print(f'Player: {player}')
    print(f'Computer: {computer}')
    if player == computer:
        print('Tie!')
        return 0
    elif player == 'rock' and computer == 'scissors':
        print('Player wins!')
        return 1
    elif player == 'scissors' and computer == 'paper':
        print('Player wins!')
        return 1
    elif player == 'paper' and computer == 'rock':
        print('Player wins!')
        return 1
    else:
        print('Computer wins!')
        return -1

#By the end of each round, the player can choose whether to play again.

def play_game():
    score = 0
    while True:
        score += play_round()
        print(f'Score: {score}')
        play_again = input('Play again? (yes/no): ')
        if play_again != 'yes':
            break
    print(f'Final score: {score}')

play_game()