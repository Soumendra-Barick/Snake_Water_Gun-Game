import random
'''
1 for Snake
-1 for Water
0 for Gun
'''
computer = random.choice([1,0,-1])   # computer choice
youstr = input("Enter your choice: ") # user choice
youdict = {"s":1, "w":-1, "g":0}
reversedict = {1:"Snake", -1:"Water", 0:"Gun"}
you = youdict[youstr]

# After this 2 variables : computer and you

print(f"you chose {reversedict[you]}\ncomputer chose {reversedict[computer]}")

if(computer==you):
    print("It is Draw!")
else:
    '''
    if(computer == 1 and you == -1): (computer - you) = 2
        print("You lose!")

    elif(computer == 1 and you == 0): (computer - you) = 1
        print("You win!")

    elif(computer == -1 and you == 1): (computer - you) = -2
        print("You win!")

    elif(computer == -1 and you == 0): (computer - you) = -1
        print("You lose!")

    elif(computer == 0 and you == 1): (computer - you) = -1
        print("You lose!")

    elif(computer == 0 and you == -1): (computer - you) = 1
        print("You win!")
    '''
    if((computer - you) == -1 or (computer - you) == 2):
        print("You lose!")
    else:
        print("You win!")