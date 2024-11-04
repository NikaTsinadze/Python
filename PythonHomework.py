import tkinter as tk
from tkinter import messagebox
import random

# Initialize scores
player_score = 0
computer_score = 0
tie_score = 0

# Function to determine the computer's choice
def get_computer_choice():
    return random.choice(["rock", "paper", "scissors"])

# Function to determine the winner and update the score
def determine_winner(player_choice, computer_choice):
    global player_score, computer_score, tie_score
    
    if player_choice == computer_choice:
        tie_score += 1
        return "It's a tie!"
    elif (player_choice == "rock" and computer_choice == "scissors") or \
         (player_choice == "scissors" and computer_choice == "paper") or \
         (player_choice == "paper" and computer_choice == "rock"):
        player_score += 1
        return "You win!"
    else:
        computer_score += 1
        return "Computer wins!"

# Function to handle the button click, display the result, and update the score
def play_game(player_choice):
    computer_choice = get_computer_choice()
    result = determine_winner(player_choice, computer_choice)
    
    result_text = f"You chose {player_choice}\nComputer chose {computer_choice}\n\n{result}"
    messagebox.showinfo("Game Result", result_text)
    
    # Update the score label
    update_score_label()

# Function to update the score display
def update_score_label():
    score_label.config(text=f"Player: {player_score}   Computer: {computer_score}   Ties: {tie_score}")

# Function to reset scores
def reset_scores():
    global player_score, computer_score, tie_score
    player_score = 0
    computer_score = 0
    tie_score = 0
    update_score_label()

# Setting up the main window
root = tk.Tk()
root.title("Rock, Paper, Scissors")
root.geometry("300x300")

# Title label
title_label = tk.Label(root, text="Rock, Paper, Scissors", font=("Arial", 16))
title_label.pack(pady=10)

# Score label
score_label = tk.Label(root, text=f"Player: {player_score}   Computer: {computer_score}   Ties: {tie_score}", font=("Arial", 12))
score_label.pack(pady=10)

# Button for Rock
rock_button = tk.Button(root, text="Rock", width=10, command=lambda: play_game("rock"))
rock_button.pack(pady=5)

# Button for Paper
paper_button = tk.Button(root, text="Paper", width=10, command=lambda: play_game("paper"))
paper_button.pack(pady=5)

# Button for Scissors
scissors_button = tk.Button(root, text="Scissors", width=10, command=lambda: play_game("scissors"))
scissors_button.pack(pady=5)

# Reset scores button
reset_button = tk.Button(root, text="Reset Scores", width=10, command=reset_scores)
reset_button.pack(pady=15)

# Run the main event loop
root.mainloop()


