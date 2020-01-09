# Hello-world
# Author-Shudhanshu raj

# Write a programme where the computer randomly generates a number between 0 and 20.
# The user needs to guess what the number is.
# If the user guesses wrong, tell them their guess is either too high, or too low.
# This will get you started with the random library if you have



import random

# function defined to increase the toughness level of game 
def Level(a,number_trial):
    global x
    global count
    print('Guess between 1 to ', a)
   # random.randrange(1,a,1) generate random number in range of 1 and a 
    x=random.randrange(1,a,1)
    count=number_trial


x=0
a=20
count=0
j=1
# game starts here
print('Level ',j)
Level(a,5)
i=0
while(1):
   # if count increases maximum numbers of trial than loop will break
    if i==count :
        print('Ooops! You Lost')
        break
    y = int(input('Guess a number: '))
    if x==y:
        print('Congratulation\'s! you guessed it correctly.')
        j+=1
   # since user won this game, level will be incresed
        print('Level ',j)
        i=0
        a+=10
        Level(a,count+2)
    elif x > y:
        print('The number you gussed is too low. Try again.')
    else:
        print('The number you gussed is too high. Try again.')
    i+=1
