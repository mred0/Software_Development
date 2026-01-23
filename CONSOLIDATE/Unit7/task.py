import random

number_to_guess = random.randint(1, 20)
attempts = 0
max_attempts = 5

print("Guess the Number - Game")
print("Guess a number between 1 and 20")

while attempts < max_attempts:
    guess = int(input("Enter your guess: "))
    attempts += 1

    if guess == number_to_guess:
        print("Congratulations! You guessed the correct number.")
        break
    else:
        print("Wrong guess. Try again.")

if guess != number_to_guess:
    print("You have used all attempts.")
    print("The correct number was:", number_to_guess)
