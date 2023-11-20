# import random
import random

# create three variables: rounds, wins, and losses. Start each of them off at 0.
rounds = 0
wins = 0
losses = 0

# create a function call computer_choice that will randomly pick rock, paper, or scissors
def computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# create a function called play_game that imports the three variables from above
def play_game(rounds, wins, losses):
    # create a user_choice variable that asks the user to pick rock, paper, or scissors and stores it in the variable. also make sure to make it lowercase.
    user_choice = input('Pick rock, paper, or scissors: ').lower()
    # check for input validation. if the user doesn't enter rock, paper, or scissors, print an error message and return the function.
    if user_choice not in ['rock', 'paper', 'scissors']:
        print('Invalid input. Please try again.')
        return play_game(rounds, wins, losses)
    
    # create a variable called computer and call the computer_choice function to get the computer's choice
    computer = computer_choice()

    # increment rounds by 1
    rounds += 1

    # check for a tie. if the user's choice is the same as the computer's choice, print a message saying it's a tie and return the function.
    if user_choice == computer:
        print('It\'s a tie!')
        return play_game(rounds, wins, losses)
    
    # check for a win. if the user's choice is rock and the computer's choice is scissors, or if the user's choice is paper and the computer's choice is rock, or if the user's choice is scissors and the computer's choice is paper, print a message saying the user won and increment wins by 1.
    if (user_choice == 'rock' and computer == 'scissors') or (user_choice == 'paper' and computer == 'rock') or (user_choice == 'scissors' and computer == 'paper'):
        print('You won!')
        wins += 1
        # else print a message saying the user lost and increment losses by 1.
    else:
        print('You lost!')
        losses += 1

    # call the play_again function
    play_again(rounds, wins, losses)



#create a function called play_again that imports the three variables from above
def play_again(rounds, wins, losses):
    # create a variable called play_again that asks the user if they want to play again. make sure to make it lowercase.
    play_again = input('Do you want to play again? (y/n) ').lower()
    # check for input validation. if the user doesn't enter y or n, print an error message and return the function.
    if play_again not in ['y', 'n']:
        print('Invalid input. Please try again.')
        return play_again(rounds, wins, losses)
    # if the user enters y, call the play_game function
    if play_again == 'y':
        play_game(rounds, wins, losses)
    # else print a message saying thanks for playing and print the number of rounds, wins, and losses
    else:
        print(f'Thanks for playing! Rounds: {rounds}, Wins: {wins}, Losses: {losses}')

# call the play_game function
play_game(rounds, wins, losses)