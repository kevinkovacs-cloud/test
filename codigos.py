"""
print('hello world')

a, b = 1, 2

print(a, b)

type(a)

if a == 1:
    print("hola")

"""
"""
i = 2
while i<= 10:
    print(i)
    i=i+1

if i == 11:
    print("es 11 el valor de i boludo")
else: print(i)

"""

#for i in range(4, 11):  #i toma los valores del rango, hasta 11 exclusive.
#   print(i)

### entonces, se hace:

#for i in range(1,10):
#   print(i)

#print(i) #el valor actual de i se transformo, ahora es 11 porque lo cree con el loop "for"

#x = "holaa" #en realidad no es necesario decirle el valor de x, ya que el "for" pone el rango entre comillas. la variable es al pedo

#for x in range(1,19):
#    print(x)
#
#for y in range(1,19):
#    print(y)
"""
for y in range(1,20,2):
    print(y)
"""
"""
def mifuncion():
    nombre = input("Ingrese su nombre: ")
    print(f"hola {nombre}")

mifuncion()

def calcular_edad(annio_nacimiento):
    edad = 2020 - annio_nacimiento 
    print(edad)
 #necesito que sea un numero lo de abajo
annio_nacimiento = input("Ingrese año de nacimiento: ")
calcular_edad(int(annio_nacimiento))

 PARA STRINGS TODO LO DE ABAJO
name = "Bro"

print(len(name))
print(name.find("o"))
print(name.capitalize())
print(name.upper())
print(name.lower())
print(name.isdigit())
print(name.isalpha())
print(name.count("o"))
print(name.replace("o","a"))
print(name)
print(name*3)

typecasting

conver data value to another data value (typecasting)

x = 1 #int
y =2.0 #float
z = "3" #string

print(int(y))

y=int(y)
print(type(y))
print(y*3)
print(z*3)

x = float(x)
print(type(x))

THIS IS THE BASICS OF USER INPUT:

#accept user input (input function)

#let's ask for somebody's name

name = input("What is your name?: ")
#age = input("How old are you?: ")
#we cannot use str for math, so:
age = int(input("How old are you?: "))
height = input("How tall are you?: ")

#age = age + 1 (we don't need to do it)

print("Hello  "+name)
print("You are "+str(age)+" years old")
print("You are "+str(height)+"cm tall")

#but we can't say i'm 11.5 years old. just a whole number
#float data type come in, with the Height.

# a few useful functions related to numbers in python

age = int(input("Tu edad es: "))

#print(age)

if age >= 30:
    print("Tenes mas de 30")

else: 
    print("Sos un pibito")

if age >= 30:
    print("Tenes mas de 30")
elif age == 0:
    print("TENES CERO AÑES")
elif age < 0:
    print("Ni naciste gil")
else: 
    print("Sos un pibito")

temp = int(input("Cual es la temperatura?: "))

if temp > 3 and temp <= 30: #tambien puedo usar "or"
    print("la temperatura es una mierda")
    print("hola todo piola")
    print("chau")

name = None 

while not name:
    name = input("Enter your name: ")

print("Hello "+name)

# WHILE LOOP = ILIMITADO
# FOR LOOP = LIMITADO

for i in range(10):
    print(i+1)

for i in range(50,100+1,2):
    print(i)

for i in "Kevin Kovacs":
    print(i)

import time

for seconds in range(10,0,-1): #count down
    print(seconds)
    time.sleep(1)
print("Happy new year!")

#nested loops: un loop adentro de otro loop

rows = int(input("How many rows?: "))
columns = int(input("How many columns?: "))
symbol = input("Enter a symbol: ")

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")
    print()

#Loop control Statements: change loop from its normal sequence

#break: #to terminate the loop entirely
while True:
    name = input("Enter your name: ")
    if name != "":
        break


phone_number = "123-456-7890"

for i in phone_number:
    if i == "-": 
        continue
    print(i, end="")

#last but not lease

for i in range(1,21):
    
    if i == 13:
        pass
    else:
        print(i)

# lists

food = ["pizza", "hamburguer", "hotdog", "spaghetti", "pudding"]

food[0] = "sushi"

food.append("ice cream")
food.remove("hotdog")
food.pop()
food.insert(0,"cake")
food.sort()
food.clear()

#Tuples

student = ("Bro", 21, "male")

student.count() 
print(student.index("male"))

for x in student:
    print(x)

if "Bro" in student:
    print("Bro is here")

#set

utensils = {"fork", "spoon", "knife"}

for x in utensils:
    print(x) #it may be in different order

#if i have another set (for example dishes)
#i can code:

print(utensils.difference(dishes))
print(utensils.intersection(dishes)) #in common

#dictionaries: allow us to acces a value quickly

capitals = {'USA': 'Washington DC',
            'India': 'New Dehli',
            'China':'Beijing',
            'Russia':'Moscow'}
#print(capitals['Russia'])

#if doesn't exist: print(capitals[Germany]) but better we can do:
#print(capitals.get('Germany'))
#print(capitals.keys())
#print(capitals.items())
#print(capitals.values())

#for key,value in capitals.items():
#    print(key,value)

#for x in capitals.items():
#    print(x)

#for updating dictionaries:
capitals.update({'Germany':'Berlin'})
capitals.update({'USA':'Las Vegas'})
capitals.pop('China')
capitals.clear()

#index operator[] = gives access to a sequence's element (str, list, tuples)
name = "bro Code"
#if(name[0].islower()):#si esta en minuscula, lo cual no
#    name = name.capitalize()

first_name = name[0:3].upper()
last_name = name[4:].lower() #next blank
#si fuera -1 seria de atras para adelante
print(name)
print(first_name)
print(last_name)


#FUNCTIONS : a block of code which is executed only when it is called

#def hello():
    #print("hello!"+name)
#but name is not defined
#hello()

def hello(name):
    print("hello!"+name)
    print("have a nice day!")
hello("Bro") #porque defino el name como "bro", le digo que va a ser

def hello(first_name, last_name, age):
    print("hello "+first_name+" "+last_name)
    print("You are "+str(age)+" years old")
    print("Have a nice day!")

hello("Bro", "Code", 21)

#RETURN ON PYTHON
def multiply(number1, number2):
    result = number1 * number2
    return result

x = multiply(6, 8)

print(x)

# KEYWORD ARGUMENTS:

def hello(first,middle,last):
    print("Hello "+first+" "+middle+" "+last)

hello(middle= "Yoel", last= "Kovacs", first="Kevin")

#NESTED FUNCTIONS CALLS:

#instead of doing:
#num = input("Enter a whole positive number: ")
#num = float(num)
#num = abs(num)
#num = round(num)
#print(num)

#we can do this instead:

print(round(abs(float(input("Enter a whole positive number: ")))))

#SCOPE = region where it's available

def display_name():
    name = "Code" #it's a local scope, a local variable inside a function
    print(name)

# print(name) IT DOESN'T EXIST, it will give me an error.
#otherwaise, we can create a GLOBAL VARIABLE with the same name, and =! results.
"""
# * args

"""
For example, we have a function like this:
deff add(num1, num2):
     sum = sum1 + sum2
     return sum

#but, if we say print(add(1,2,3)) ya se me rompe la funcion, no se puede mas argumentos

def add(*args): #actually, "args" itsn't necessary, we can call it whatever we want
    sum = 0 
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))     #esto es una tupla
#but, we can transform it to a list:

def add(*args): #actually, "args" itsn't necessary, we can call it whatever we want
    sum = 0
    args = list(args)
    args[0] = 0 #so first value (1) will turned into 0
    for i in args:
        sum += i
    return sum

print(add(1,2,3,4,5,6))

# ** kwwargs: transform all arguments into a dictionary
# is useful so that a function can accept a varying amount of keyword arguments

#because, we can't do:
'''
def hello(first, last):
    print("Hello "+ first + " "+ last)

hello(first="Bro",middle="Dude",last="Code")

# because middle is not definded in the function
'''

def hello(**names):
    #print("Hello "+kwargs['first'] + " "+ kwargs['last'])
    print("Hello",end=" ")
    for key,value in names.items():
        print(value,end=" ")

hello(title="Mr.",first="Bro", middle="Dude", last="Code")

#str.format() 

animal = "cow"
item = "moon"

#print("The "+animal+" jumped over the "+item)
print("The {} jumped over the {}".format(animal,item)) 
#print("The {1} jumped over the {0}".format("cow","moon")) #positional argument
#print("The {animal} jumped over the {item}".format(animal="cow",item="moon")) #keyword argument

text = "The {} jumped over the {}"

print(text.format(animal, item))

#RANDOM

import random

x = random.randint(1,6)
y = random.random()

myList = ['rock', 'paper', 'scissors']
z = random.choice(myList)

cards = [1, 2, 3, 4, 5, 6, 7, 8, 9, "J", "Q", "K", "A"]

random.shuffle(cards)

print(cards)
print(z)

# EXEPTION

try:
    numerator =  int(input("Enter a number to divide: "))
    denominator = int(input("Enter a number to divide by: "))
    result =  numerator / denominator
except ZeroDivisionError as e:
    print(e) #it's a standard practice
    print("You can't divide by zero! idiot!")
except ValueError as e:
    print(e)
    print("Enter only numbers plz")
except Exception as e:
    print(e)
    print("something went wrong :(")
else:
    print(result)
finally:
    print("This will always execute") 

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

# FILE DETECTION (medio al pedo porque uso el bash de linux para esto)

import os 

path = "/home/kevin/Linux/PythonPrueba"

if os.path.exists(path):
    print("That location exists!")
    if os.path.isdir(path):
        print("That is a dir")
else:
    print("It's not")

# READ A FILE

with open('hola.txt') as file:
    print(file.read())
print(file.closed) #because it's closed

#IF IT'S BAD WRITTEN:

try:
    with open('hola.tx') as file:
        print(file.read())
except FileNotFoundError:
    print("That file was not found :(")

#EDIT A FILE
text = "Yooooooooo/nThis is some text/nHave a good day!/n" #/n is new line

with open('hola.txt', 'w') as file: #w because it's write, #r is read
    file.write(text) #it overwrite what i wrote before

text = "Have anice day!/n See ya" 

with open('hola.txt', 'a') as file: 
    file.write(text) 

# COPY A FILE

#three basic functions in this module -> copyfile(), copy() (Copy permission mode), copy2()
# and the metadata with this last copy2

import shutil

shutil.copyfile('hola.txt', 'copy.txt') #souce, destination (it could be a PATH)
 
#MOVE A FILE

import os 

source = "hola.txt"
destination = "/home/kevin/Linux/PythonPrueba"

try:
    if os.path.exists(destination):
        print("There is already a file there")
    else:
        os.replace(souce,destination)
        print(source+" was moved")
except FileNotFoundError:
    print(source+" was not found")

#DELETE A FILE

import os 

name_of_file: "move_file"

try: 
    os.rmdir(name_of_file)
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You don't have permission to delete that")

#--------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------

#MODULES ON PYTHON: a file containing python code

import message as msg #name of module i created in our folder
#from messages import *
msg.hello()

# -------------------------

#quiz game

def new_game():

    guesses = [] #it's a list
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("-------------------------")
        print(key)
        for i in options[question_num-1]:
            print(i)
        guess = input("Enter (A, B, C, or D): ")
        guess = guess.upper()
        guesses.append(guess)

        correct_guesses += check_answer(questions.get(key), guess)
        question_num += 1

    display_score(correct_guesses, guesses)

# -------------------------
def check_answer(answer, guess):

    if answer == guess:
        print("CORRECT!")
        return 1
    else:
        print("WRONG!")
        return 0

# -------------------------
def display_score(correct_guesses, guesses):
    print("-------------------------")
    print("RESULTS")
    print("-------------------------")

    print("Answers: ", end="")
    for i in questions:
        print(questions.get(i), end=" ")
    print()

    print("Guesses: ", end="")
    for i in guesses:
        print(i, end=" ")
    print()

    score = int((correct_guesses/len(questions))*100)
    print("Your score is: "+str(score)+"%")

# -------------------------
def play_again():

    response = input("Do you want to play again? (yes or no): ")
    response = response.upper()

    if response == "YES":
        return True
    else:
        return False
# -------------------------


questions = {
 "Who created Python?: ": "A",
 "What year was Python created?: ": "B",
 "Python is tributed to which comedy group?: ": "C",
 "Is the Earth round?: ": "A"
}

options = [["A. Guido van Rossum", "B. Elon Musk", "C. Bill Gates", "D. Mark Zuckerburg"],
          ["A. 1989", "B. 1991", "C. 2000", "D. 2016"],
          ["A. Lonely Island", "B. Smosh", "C. Monty Python", "D. SNL"],
          ["A. True","B. False", "C. sometimes", "D. What's Earth?"]]

new_game()

while play_again():
    new_game()

print("Byeeeeee!") #if player doesn't wanna play anymore

#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------
#---------------------------------------------------------------------------

#PYTHON OBJET ORIENTED PROGRAMMING (OOP) -> assign attributes and methods

#class Car:
#    pass #as a placeholder
#if your class is too large, you should consider create a separate module
#so, in the python folder i create a module named "Car"

from car import Car 

car_1 = Car("Chevy","Corvette",2021,"blue")

print(car_1.make)
print(car_1.model)
print(car_1.year)
print(car_1.color)

car_1.drive() #and we don't need to say (self) we don't need to pass for this argument
#The __init__() function is called automatically every time the class is being used
#  to create a new object.

car_1.stop()

# CLASS VARIABLES

from car import Car 

car_1 = Car("Chevy","Corvette",2021,"blue")
car_2 = Car("Ford","Mustang",2022,"red")

car_1.wheels = 2
#car.wheels = 2 #it changes everything after this line of code

print(car_1.wheels)
print(car_2.wheels) #default amount of wheels

#inhertirance: to receive
#Animal -> alive, eat(), sleep() -> 1) Rabbit -> run(), 2) Fish, swim(), 3) Hawk, fly().
#animal.py

#multilevel inheritance = when a derived (child) class inherits another derived (child) class

class Organism:

    alive = True

class Animal(Organism):

    def eat(self):
        print("This animal is eating")

class Dog(Animal):
    def bark(self):
        print("This dog is barking")

dog = Dog()
print(dog.alive)
dog.eat()

"""



