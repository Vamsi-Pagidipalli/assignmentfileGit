import random

# Function to greet the user
def greet_user():
    print("Welcome to Rock-Paper-Scissors!")
    print("Let's play! Here are the rules:")
    print("Rock beats Scissors, Scissors beats Paper, Paper beats Rock.")
    print("Type 'rock', 'paper', or 'scissors' to play. Let's begin!\n")

# Function to get the computer's choice
def get_computer_choice():
    return random.choice(['rock', 'paper', 'scissors'])

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "tie"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "user"
    else:
        return "computer"

# Main function to play the game
def play_game():
    greet_user()
    while True:
        user_choice = input("Enter your choice (rock, paper, or scissors): ").lower()
        if user_choice not in ['rock', 'paper', 'scissors']:
            print("Invalid input. Please try again.")
            continue
        computer_choice = get_computer_choice()
        print(f"Computer chose: {computer_choice}")
        
        winner = determine_winner(user_choice, computer_choice)
        if winner == "tie":
            print("It's a tie! Rematching...\n")
        elif winner == "user":
            print("Congratulations! You win!")
            break
        else:
            print("Computer wins! Better luck next time!")
            break

if _name_ == "_main_":
    play_game()