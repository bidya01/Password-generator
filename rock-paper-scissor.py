import random
print('Rules are as follows:\n Rock vs paper ->Paper wins \n Rock vs scissors -> Rock wins\n Paper vs scissor ->Scissor wins\n')
while(True):
    c=random.randint(1,4)
    choice=int(input("Enter your choice:\n 1.Rock\n 2.Paper\n 3.Scissors\n"))
    if(c==1):
        print("Computer's choice is rock!")
    elif(c==2):
        print("Computer's choice is paper!")
    elif(c==3):
        print("Computer's choice is scissor!")
    if( (c==1 and choice ==2) or (choice==1 and c==2)):
        if(choice ==1):
            print("Computer wins!")
        else:
            print("You win!")
    elif( (c==1 and choice ==3) or (choice==1 and c==3)):
        if(choice ==3):
            print("Computer wins!")
        else:
            print("You win!")
    elif( (c==2 and choice ==3) or (choice==2 and c==3)):
        if(choice ==2):
            print("Computer wins!")
        else:
            print("You win!")
    elif(c==choice):
            print("It's a draw!")
    ans=input("Do you want to play again?Type Yes/No")
    if(ans=="No"):
        break
    
    
    
