"""
Multiplication Game Script
This script runs a console-based multiplication game. The game presents multiplication questions based on the chosen difficulty level. The player's performance is evaluated based on the number of correct answers, time taken, and answers per second.
"""

import random
import time

def generate_question(difficulty):
    """
    Generate a multiplication question based on difficulty level.

    Parameters:
    difficulty (int): Difficulty level of the game. 
                      1-Easy (1x1), 2-Medium (1x2), 3-Hard (1x3), 4-Very Hard (2x2).

    Returns:
    tuple: A tuple containing two integers that represent the multiplication question.
    
    Raises:
    ValueError: If an invalid difficulty level is passed.
    """
    if difficulty == 1:
        return random.randint(1, 9), random.randint(1, 9)
    elif difficulty == 2:
        return random.randint(1, 9), random.randint(10, 99)
    elif difficulty == 3:
        return random.randint(1, 9), random.randint(100, 999)
    elif difficulty == 4:
        return random.randint(10, 99), random.randint(10, 99)

def get_valid_input(prompt):
    """
    Get valid input from the user. Ensures input is either a number, 'q' for quitting, or empty for skipping.

    Parameters:
    prompt (str): The input prompt to be displayed to the user.

    Returns:
    int, str, or None: The validated user input. It's an integer (user's answer), 'q' (to quit), or None (to skip).
    """
    while True:
        user_input = input(prompt)
        if user_input.lower() == 'q':
            return 'q'
        if user_input == '':
            return None
        try:
            return int(user_input)
        except ValueError:
            print("Invalid input. Please enter a number, or press Enter to skip.")

def start_game(difficulty):
    """
    Start the multiplication game with the given difficulty level.

    Parameters:
    difficulty (int): The difficulty level of the game.

    Returns:
    tuple: A tuple containing the number of correct answers, total attempts, and total time taken.
    """
    correct_answers = 0
    attempts = 0
    start_time = time.time()

    while True:
        x, y = generate_question(difficulty)
        while True:  # Loop to repeat the same question on incorrect answer
            print("\n" + "-" * 20)  # Separating lines for clarity of question display
            answer = get_valid_input(f"What is {x} * {y}? Type 'q' to quit or press Enter to skip: ")

            if answer == 'q':
                time_taken = time.time() - start_time
                return correct_answers, attempts, time_taken
            if answer is None:  # Skip question
                break
            if answer == x * y:
                print("Correct!")
                correct_answers += 1
                break
            else:
                print("Incorrect. Try again.")

        attempts += 1

def display_score(correct_answers, attempts, time_taken):
    """
    Display the final score of the game.

    Parameters:
    correct_answers (int): Number of correct answers given by the player.
    attempts (int): Total number of questions attempted.
    time_taken (float): Total time taken by the player in seconds.
    """
    percentage_correct = (correct_answers / attempts * 100) if attempts != 0 else 0
    answers_per_second = correct_answers / time_taken if time_taken > 0 else 0
    print("\nGame Over")
    print(f"Time Taken: {time_taken:.2f} seconds")
    print(f"Questions Attempted: {attempts}")
    print(f"Correct Answers: {correct_answers}")
    print(f"Accuracy: {percentage_correct:.2f}%")
    print(f"Answers Per Second: {answers_per_second:.2f}")

def main():
    """
    Main function to run the multiplication game. Handles the game's setup and execution.
    """
    print("Welcome to the Multiplication Game!")
    while True:
        try:
            difficulty = int(input("Choose difficulty (1-Easy, 2-Medium, 3-Hard, 4-Very Hard): "))
            if 1 <= difficulty <= 4:
                break
            else:
                print("Invalid difficulty. Please choose a number between 1 and 4.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    correct_answers, attempts, time_taken = start_game(difficulty)
    display_score(correct_answers, attempts, time_taken)

if __name__ == "__main__":
    main()

