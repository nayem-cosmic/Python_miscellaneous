cube = 27
epsilon = 0.01
guess = 0
increment = 0.0001
num_guesses = 0

while abs(guess**3 - cube) >= epsilon:
    guess += increment
    num_guesses += 1

print("Number of guess:", num_guesses)

print(guess, "is close to cube root of", cube)


