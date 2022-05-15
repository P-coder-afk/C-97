import random
number = random.randint(1, 10)
guesses = 0
print("This is a number guessing game")
print("Guess the number: ")

while (guesses < 3):
    guess = int(input())
    guesses += 1
    if (guess < number):
        print('Your guess is too low')
    if (guess > number):
        print('Your guess is too high')
    if (guess == number):
        break
if (guess == number):
    print('Yay!!!You guessed the number ')
else:
    print('You did not guess the number, The number was ' ,number)