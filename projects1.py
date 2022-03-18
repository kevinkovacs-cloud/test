'''

print("Welcome to my computer quiz!")

playing = input("Do you wanna play this game? ")

#if True:
#   quit() #whatever i write, it will quit

if playing != "yes":
    quit() #always indented after statment

print("Okay! Let's play :)") #if i say no, it won't appear

answer = input("What does CPU stand for? ")
if answer == "central processing unit":
    print('Correct!') #single quotes, it doesn't matter which you use
else: 
    print("Incorrect!") #if not last one, this one
    print("you're completely wrong, shame on you!")

answer = input("What does GPU stand for? ")
if answer == "graphics processing unit":
    print('Correct!') 
else: 
    print("Incorrect!") 

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!') 
else: 
    print("Incorrect!") 

answer = input("What does PSU stand for? ")
if answer == "power supply":
    print('Correct!')  
else: 
    print("Incorrect!") 

'''
''' 
print("Welcome to my computer quiz!") #CORRECTING LOWER AND UPPER CASE

playing = input("Do you wanna play this game? ")

#if True:
#   quit() #whatever i write, it will quit

if playing.lower() != "yes": #but it's not in capital letters or something like user can write
    quit() #always indented after statment

print("Okay! Let's play :)") #if i say no, it won't appear
score = 0

answer = input("What does CPU stand for? ")
if answer.lower == "central processing unit":
    print('Correct!') #single quotes, it doesn't matter which you use
    score += 1
else: 
    print("Incorrect!") #if not last one, this one
    print("you're completely wrong, shame on you!")

answer = input("What does GPU stand for? ").lower() #we can write it here
if answer == "graphics processing unit":
    print('Correct!')
    score += 1 
else: 
    print("Incorrect!") 

answer = input("What does RAM stand for? ")
if answer == "random access memory":
    print('Correct!')
    score += 1 
else: 
    print("Incorrect!") 

answer = input("What does PSU stand for? ")
if answer == "power supply":
    print('Correct!')
    score += 1  
else: 
    print("Incorrect!") 

print ("You got " + str(score) + " questions correct!")
print ("You got " + str((score/4))*100) + "%") #without spaces #/number of questions
# "tim" + "1", no puedo hacer "tim" + 1. no podes sumar diferentes tipos.

'''


#ANOTHER PROJECT

import random

#all funtionalities in random
#this is built by default

#r = print(random.randrange(-5, 11)) #it's not intuitive for beginners but that's how it works
#print(r) 

#t = random.randint(-5,11)
#print(t)

top_of_range = input("Type a number: ")

if top_of_range.isdigit(): #if it's digit
    top_of_range = int(top_of_range) #we want to conver "25" into 25 (if that, it will convert)

    if top_of_range <= 0:
        print('Please type a number larger than 0 next time')
        quit()
else: 
    print('Please type a number next time.')
    quit()


random_number = random.randint(0, top_of_range)
guesses = 0

while True:
    guesses += 1
    user_guess = input("Make a guess: ")
    if user_guess.isdigit(): 
        user_guess = int(user_guess)
    else: 
        print('Please type a number next time.')
        continue #bring us back to the begin of the loop
    
    if user_guess == random_number:
        print("You got it!")
        break
    elif user_guess > random_number:
        print("Your were above the number")
    else:
        print("You were below the number!")

#print("You got it in", guesses, "guesses") #with a comma you don't need spaces. 
#print("You got in in " + str(guesses) + " guesses")
print("You got it in", guesses, "guesses") #with a comma you don't need spaces. 
#any of this will work the same way
















































