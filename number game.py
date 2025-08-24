import random
playing = True
number = str(random.randint(10, 20))

print(" \n Welcome to the number guessing game")
print("\n Rules: \n")

print("I will guess a number from 0 to 20 and you have to guess the number one digit at a time \n")

print("The game will end when you will be awarded hero \n")

while playing:
    guess = input("Enter your guess: ")
    if number == guess:
        print ("You are a hero!")
        print("The number was " , number)
        break

    else:
        print("Your guess is wrong, try again! \n")
        print("The number was " , number)