import random
number=random.randint(1,21)
guess_count=0
while(guess_count<5):
    guess=int(input("Enter your guess"))
    if(guess==number):
        print("You win! The number is",number)
        break
    elif(guess<number):
        print("Too low!")
    elif(guess>number):
        print("Too high!")
    guess_count=guess_count+1
else:
    print("You are wrong! The number is ",number)
    

    
