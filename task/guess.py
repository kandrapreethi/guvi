def ran():
    hidden = random.randint(1, 5) 
    guess = int(input("Please enter your guess: "))
    if guess == hidden:
        print("Won!")
    elif guess < hidden:
        print("Your guess is too low")
    else:
        print("Your guess is too high")
    return guess

import random
ran()
