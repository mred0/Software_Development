import random  # built-in library for generate random numbers 

# Here We are Generating a random number between 1 and 10 

secret_number = random.randint(1, 10) 
  

print("Guess the number between 1 and 10!") 


while True: 

    # Geting user input 

    guess = input("Enter your guess: ") 

    # Check if input is a number or not

    if not guess.isdigit(): 

        print("Please enter a valid number.") 

        continue 

    guess = int(guess) 


    # Comparing guess with the secret number 

    if guess < secret_number: 

        print("Too low! Try again.") 

    elif guess > secret_number: 

        print("Too high! Try again.") 

    else: 

        print("Correct! You guessed the number.") 

        break 
