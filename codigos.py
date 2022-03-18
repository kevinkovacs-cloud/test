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

"""







