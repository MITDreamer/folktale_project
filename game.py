import random

def guess_the_number():
    print("Welcome to Guess The Number!")
    print("The number is between 1 through 100")
    
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    attempts = 0
    
    # Main game loop
    while True:
        user_input = input("\nEnter your guess: ")
        
        # Validation: Check if the input is actually a number
        try:
            guess = int(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid whole number.")
            continue
            
        # Check the user's guess against the secret number
        if guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            print(f"Congratulations! You guessed the number! The number was {secret_number}!")
            break

# Run the game
if __name__ == "__main__":
    guess_the_number()