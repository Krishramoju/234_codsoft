def calculator():
    print("Simple Calculator")
    print("Choose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")

    # Get user input
    operation = input("Enter the operation (1/2/3/4): ")
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))

    # Perform the calculation
    if operation == '1':
        result = num1 + num2
        print(f"{num1} + {num2} = {result}")
    elif operation == '2':
        result = num1 - num2
        print(f"{num1} - {num2} = {result}")
    elif operation == '3':
        result = num1 * num2
        print(f"{num1} * {num2} = {result}")
    elif operation == '4':
        if num2 != 0:
            result = num1 / num2
            print(f"{num1} / {num2} = {result}")
        else:
            print("Error: Division by zero is not allowed.")
    else:
        print("Invalid operation choice.")

# Run the calculator
calculator()



import random
import string

def generate_password():
    print("Password Generator")

    # Get user input for the desired password length
    length = int(input("Enter the desired length of the password: "))

    # Define the characters to use in the password
    characters = string.ascii_letters + string.digits + string.punctuation

    # Generate a random password
    password = ''.join(random.choice(characters) for i in range(length))

    # Display the generated password
    print(f"Generated password: {password}")

# Run the password generator
generate_password()




import random

def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    return random.choice(choices)

def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'scissors' and computer_choice == 'paper') or \
         (user_choice == 'paper' and computer_choice == 'rock'):
        return "You win!"
    else:
        return "You lose!"

def play_game():
    user_score = 0
    computer_score = 0

    while True:
        print("\nRock, Paper, Scissors Game")
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        computer_choice = get_computer_choice()

        print(f"You chose: {user_choice}")
        print(f"Computer chose: {computer_choice}")

        result = determine_winner(user_choice, computer_choice)
        print(result)

        if result == "You win!":
            user_score += 1
        elif result == "You lose!":
            computer_score += 1

        print(f"Score -> You: {user_score} | Computer: {computer_score}")

        play_again = input("Do you want to play again? (yes/no): ").lower()
        if play_again != 'yes':
            break

    print("Thanks for playing!")

# Run the Rock, Paper, Scissors game
play_game()
