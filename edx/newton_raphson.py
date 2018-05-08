# using Newton-Raphson method to solve a simple polynomial
# x^2 - c = 0

c = 27
epsilon = 0.00001
guess = c/2.0
num_guesses = 0

while abs(guess**2-c) >= epsilon:
    num_guesses += 1
    guess = guess - (guess**2-c)/(2*guess)

print("Number of guesses:", num_guesses)
print("Square root of", c, "is", guess)
