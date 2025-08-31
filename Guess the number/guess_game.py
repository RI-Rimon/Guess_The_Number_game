import random
n = random.randint (1, 100)
a = -1
guesses = 0
while( a!= n):
    guesses += 1
    a = int(input("Guess the number: "))
    if (a>n):
        print("Enter lower number")
    else:
        print("Enter higher number")


print(f"You guessed the correct number in {guesses} attempts")     