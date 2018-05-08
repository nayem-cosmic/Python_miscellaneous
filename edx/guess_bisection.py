high = 100
low = 0
ans = int((high+low)/2)

print("Please think of a number between 0 and 100!")

while True:
    print("Is your secret number " + str(ans) + "?")
    c = input("Enter 'h' to indicate the guess is too high. Enter 'l' to indicate the guess is too low. Enter 'c' to indicate I guessed correctly.")
    if c == 'h':
        high = ans
    elif c == 'l':
        low = ans
    elif c == 'c':
        print("Game over. Your secret number was: ", str(ans))
        break
    else:
        print("Sorry, I did not understand your input.")
    ans = int((high+low)/2)
