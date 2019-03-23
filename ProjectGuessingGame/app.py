secretNumumber = 9
guessCount=1;
guessLimit=3;

while guessCount <= guessLimit:
    userInput = int(input("Guess Magic Number: "))
    guessCount = guessCount + 1
    if userInput == secretNumumber:
        print('You Won!')
        break
else:
    print('Sorry, you failed to guess!')