import random

print("Number Guessing Game")

number = random.randint(1, 9)

chances =  0

print("Guess a number (between 1 and 9):")

while chances < 5:
    guess = int(input("Enter your guess:"))

    if guess == number:
        print("Congratulations, you guessed the number!!!")
    
    elif guess < number:
        print("Your guess was too low. Guess a number that it higher than", guess)
    
    else:
        print("Your guess was too high. Guess a number that is lower than", guess)

    
    
    
if not chances:
        print("YOU LOSE!!! The number is ", number)



