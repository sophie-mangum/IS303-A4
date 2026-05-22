'''
Sophie Mangum
IS 303 - A04

Dice Game
This program lets the user play a dice game against the computer.
The higher roll wins each round and the program tracks the score.

Inputs:
- Number of rounds (int)
- User choice to play again (string)

Processes:
- get_positive_int(prompt): keeps asking until user enters a valid positive integer
- roll_die(): returns a random number between 1 and 6
- play_round(round_number): rolls dice for player and computer and returns winner
- determine_winner(player_roll, computer_roll): returns the round winner
- display_scoreboard(player_score, computer_score, ties): prints current scores
- display_final_results(player_score, computer_score, ties): prints final game summary

Outputs:
- Dice roll results
- Round winners
- Final scoreboard
'''

import random

# Functions

def get_positive_int(prompt):
    """Get a valid positive integer from the user."""
    while True:
        try:
            value = int(input(prompt))

            if value <= 0:
                print("Please enter a positive number.")
            else:
                return value

        except ValueError:
            print("Invalid input. Please enter a whole number.")


def roll_die():
    """Return a random die roll between 1 and 6."""
    return random.randint(1, 6)


def determine_winner(player_roll, computer_roll):
    """Determine the winner of a round."""
    if player_roll > computer_roll:
        return "Player"
    elif computer_roll > player_roll:
        return "Computer"
    else:
        return "Tie"


def play_round(round_number):
    """Play one round and return the winner."""
    print(f"\n--- Round {round_number} ---")

    player_roll = roll_die()
    computer_roll = roll_die()

    print(f"Player rolled: {player_roll}")
    print(f"Computer rolled: {computer_roll}")

    winner = determine_winner(player_roll, computer_roll)

    if winner == "Tie":
        print("This round is a tie!")
    else:
        print(f"{winner} wins the round!")

    return winner


def display_scoreboard(player_score, computer_score, ties):
    """Display the current scoreboard."""
    print("\n=== Scoreboard ===")
    print(f"Player Wins: {player_score}")
    print(f"Computer Wins: {computer_score}")
    print(f"Ties: {ties}")


def display_final_results(player_score, computer_score, ties):
    """Display the final game results."""
    print("\n=== Final Results ===")

    display_scoreboard(player_score, computer_score, ties)

    if player_score > computer_score:
        print("Overall Winner: Player")
    elif computer_score > player_score:
        print("Overall Winner: Computer")
    else:
        print("The game ended in a tie!")


# Main flow

print("=== Dice Game ===")

num_rounds = get_positive_int("How many rounds would you like to play? ")

player_score = 0
computer_score = 0
ties = 0

for round_num in range(1, num_rounds + 1):

    winner = play_round(round_num)

    if winner == "Player":
        player_score += 1
    elif winner == "Computer":
        computer_score += 1
    else:
        ties += 1

display_final_results(player_score, computer_score, ties)
