import random
#here I imported random libary
print("Welcome to the random choice")
rn=int(input("Enter the number of things: "))
#rn is the input range of things
for rn in range(0 , rn):
    things=input("Enter the thing: ")
    #And i am aadding for loop range 0 to rn input and i take input from the user for rn times
random=random.randint(1,rn)
#And i adding the random and randint to think a number between 1 to rn
print(random)
#And finally i printed the output 