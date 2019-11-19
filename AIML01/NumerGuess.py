import random
attempt=0
guesscount =0
print("****** Welcome to Number Guesser Game ******")
chances =int(input("How many turns you want to play :"))
print(" You selected to play "+ str(chances) + " times. Lets start")
while(attempt<chances):
    print("****GAME "+ str(attempt) +" ****")
    guess = int(input("Enter a number between  1 to 25: "))
    n = random.randint(1, 25)
    atcount=1
    while n != "guess":
        if guess < n:
            print ("Too low")
            atcount=atcount+1
            guess = int(input("Try Again: "))
        elif guess > n:
            print ("Too high")
            guess = int(input("Try Again : "))
            atcount=atcount+1
        else:
            print ("you guessed it Correctly in " + str(atcount) + " Attempts !!!")
            break
    attempt=attempt+1
print("This Gamme is over. Thanks for Playing")