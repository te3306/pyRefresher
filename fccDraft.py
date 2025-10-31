# Simple Hello World Program:
print("Hello World")

print("\n")




# Draw A Shape:
print("\n")

print("     /")
print("    /")
print("   /")
print("  /")
print(" / ")

print("\n")




# Variables And Data Types:
print("There once was a man named George, ")
print("he was 70 years old. ")
print("He really liked the name George, ")
print("but didnt like being 70.")


print("\n")




# Update Variables:
character_name = "John"
character_age = "35"

print("There once was a man named " + character_name + ", ")
print("he was " + character_age + " years old. ")
print("he really liked the name " + character_age + ".")


print("\n")




# Working With Strings:
phrase = "Giraffe Academy"
print(phrase + " is cool.")

print("\n")




# Strings + Functions:

# Lower Case:
phrase = "Giraffe Academy"
print(phrase.lower())

print("\n")




# Upper Case:
phrase = "Giraffe Academy"
print(phrase.upper())

print("\n")




# Check If String Is Upper Or Lower:
phrase = "Giraffe Academy"
print(phrase.isupper())  #upper - will return False
print(phrase.islower())  #lower - will return False

phrase = "LEBRON JAMES"
print(phrase.islower())
print(phrase.isupper())

phrase = "damian lillard"
print(phrase.isupper())
print(phrase.islower())




# Upper, Lower, isupper, islower:
phrase = "stephen curry"
print(phrase.upper().isupper())

phrase = "LONZO BALL"
print(phrase.lower().islower())

print("\n")




# Length Function:
phrase = "How long is this string?"
print(len(phrase))

phrase = "The len() function in Python is a powerful and efficient tool used to determine the number of items in objects, such as sequences or collections."
print(len(phrase))

print("\n")




# Specify The Length Of An Index:
phrase= "Giraffe Academy"
print(phrase[0])

phrase = "TaRon J. Evans"
print(phrase[4])

phrase= "XXXTENTACION"
print(phrase[6])

print("\n")




# Using The Index Function:
phrase = "Giraffe Academy"
print(phrase.index("G"))

phrase = "World Economic Forum"
print(phrase.index("W"))

phrase= "SPY 500"
print(phrase.index("0"))


print("\n")




# Using The Replace Function:
phrase = "To be or not to think."
print(phrase.replace("think", "be"))


print("\n")




# Working With Numbers:
print(7)
print(1.0002)
print(100 + 3.77)
print(42 - 17)

print(3 * (4 + 5))
print(12 * 7 + 17) 

print("\n")

print(10 % 3) #modulus operator

print("\n")




# Converting Numbers To A String:
my_num = 5
print(my_num)

jerseyNum = 23
print(str(jerseyNum))

print("\n")

jerseyNumName = "LeBron James"
print(jerseyNumName)
print(jerseyNum)


print("\n")




# Most Common Functions Related to Numbers:

# getting the absolute value of a number:
my_num = -5
print(abs(3)) #5

tempConversion = -24
print(abs(tempConversion))

print("\n")

# power function:
my_num = -5
print(pow(3, 2)) #9


# max function:
my_num = -5
print(max(4,6)) #6

print(max(10000, 10000000000)) #10000000000


# min function:
my_num = -5
print(min(4, 6)) # 4

print(min(1, 100)) # 1


# round function:
print(round(117.2)) # 117





# Using MATH IMPORT:
# Python commands used to import specific functions, constants, or 
# all of the contents from the math module directly into your program's namespace.
from math import *


# floor function:
print(floor(1111.976))


# ceil function:
print(ceil(94378.00))


# sqrt function:
print(sqrt(3.14))
print(sqrt(9))


print("\n")


# Getting Input From Users:
name = input("Enter your name: ")
age = input("Enter your age: ")
print("Hello " + name + "! You are " + age + " years old!")

finAnalyst1 = input("Enter your employee ID to continue: ")
print("Welcome " + finAnalyst1)




# Building A Basic Calculator:

# get two numbers from a user and then print them out to the screen.
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = num1 + num2

print(result) # 777


# integer
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = int(num1) + int(num2)

print(result) # 94


# float
num1 = input("Enter a number: ")
num2 = input("Enter another number: ")
result = float(num1) + float(num2)

print(result) # 94




# Mad Libs Game:
# word game where players fill in blanks of a story with words like nouns,
#verbs, and adjectives, often leading to humorous and nonsensical results.


# Basis for application:

# print("Rodes are red")
# print("Violets are blue")
# print("I love you.")

# print("Roses are {color}")
# print("{plural noun}" + " are blue")
# print("I love " + {celwebrity}")
color = input("Enter a color")
plural_noun = input("Enter a plural noun: ")
celebrity = input("Enter a celebrity: ")

print("Roses are " + color)
print(plural_noun + " are blue")
print("I love " + celebrity)


# Original Application

# Star Trek Madlibs Application
trekDivision = input("Enter your Starfleet Division: ")
trekClass = input("Enter your Starship class: ")
trekGalQuadrant = input("Enter your Galactic Quadrants: ")

print("Your Starfleet Division is " + trekDivision)
print("Your Starship Class is " + trekClass)
print("Your Galactic Quadrant is " + trekGalQuadrant)



# Lists
friends = ["Kevin", "Karen", "Jim"]

print(friends[1]) # Karen
print(friends[-2]) # Karen


# modify element:
friends = ["LeBron James", "Kareem Abdul Jabbar", "Michael Jordan"]

friends[1] = "Stephen Curry"
print(friends[1])



# Lists (continued)

# List Basics
favActors = ["Denzel Washington", "Humphrey Bogart", "Jason Statham", "Marlon Brando", "Sidney Poitier", "Robin Williams"]

print(favActors[2]) # Jason Statham

print(favActors[-1]) # Jason Statham


print("\n")


# select a range of names from 0 to 4.
print(favActors[0:4]) # selects a range a names starting from 0 to 4.

print("\n")


# Modify Value:
favActors = ["Denzel Washington", "Humphrey Bogart", "Jason Statham", "Marlon Brando", "Sidney Poitier", "Robin Williams"]
favActors[3] = "Robert De Niro"
print(favActors[3])




# List Functions:
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim" ]

print(friends)



# Print A List:
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim" ]

print(friends)


# Extend Function:
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim" ]
friends.extend(lucky_numbers)
print(friends)

stathamMovies1 = ["Blitz", "The Meg", "SPY", "The Bank Job"]
stathamMovies2 = ["The Mechanic", "Parker", "Homefront", "Crank"]
stathamMovies2.extend(stathamMovies2)
print(stathamMovies2)


# Append Function:
# used to add a single item to the end of an existing list.
stathamMovies1 = ["Blitz", "The Meg", "SPY", "The Bank Job"]
stathamMovies2 = ["The Mechanic", "Parker", "Homefront", "Crank"]
stathamMovies2.append(stathamMovies2)
print(stathamMovies2)


# Insert Function:
# used to add an element to a list of a specified index.
stathamMovies1 = ["Blitz", "The Meg", "SPY", "The Bank Job"]
stathamMovies2 = ["The Mechanic", "Parker", "Homefront", "Crank"]
stathamMovies2.insert(3, "The Expendables")
print(stathamMovies2)


# Remove Function:
# used to remove the first occurence of a specified value from a list.
stathamMovies1 = ["Blitz", "The Meg", "SPY", "The Bank Job"]
stathamMovies2 = ["The Mechanic", "Parker", "Homefront", "Crank"]
stathamMovies2.remove("Crank")
print(stathamMovies2)


# Clear Function:
# used to remove all elements from a mutable collection, such as a list, set or dictionary.
stathamMovies1 = ["Blitz", "The Meg", "SPY", "The Bank Job"]
stathamMovies2 = ["The Mechanic", "Parker", "Homefront", "Crank"]
stathamMovies2.clear("Crank")
print(stathamMovies2)


# Pop Function:
# available for both lists and dictionaries, used to remove and return an element.
stathamMovies1 = ["Blitz", "The Meg", "SPY", "The Bank Job"]
stathamMovies2 = ["The Mechanic", "Parker", "Homefront", "Crank"]
stathamMovies2.pop()
print(stathamMovies2) # removed last element from list.


# Index Function:
# used to find the position (index) of the first occurrence
# of a specified element within the sequence.
stathamMovies1 = ["Blitz", "The Meg", "SPY", "The Bank Job"]
stathamMovies2 = ["The Mechanic", "Parker", "Homefront", "Crank"]
stathamMovies2.pop()
print(stathamMovies2)


# List Functions - continued:
lucky_numbers = [4, 8, 15, 16, 23, 42]
friends = ["Kevin", "Karen", "Jim", "Oscar", "Tim"]

print(friends.index("Kevin")) # 0

print("\n")

greatestLinebackers1 = [50, 58, 51, 52, 56 ]
greatestLinebackers2 = ["Mike Singletary", "Jack Lambert", "Dick Butkus", "Ray Lewis", "Lawrence Taylor"]
print(greatestLinebackers2.index("Dick Butkus")) # 2

print("\n")


# Count Function:
# used for sequencing data types like strings, lists, and tuples. 
# used to determine the number of times a specified element or substring appears within the sequence.
greatestLinebackers1 = [50, 58, 51, 52, 56 ]
greatestLinebackers2 = ["Mike Singletary", "Jack Lambert", "Jack Lambert", "Ray Lewis", "Lawrence Taylor"]
print(greatestLinebackers2.count("Jack Lambert"))


# Sort Function
# takes any iterable (lists,tuples, set, strings, etc.) as input and returns a new sorted list. It does not modify the original iterable.
greatestLinebackers2 = ["Mike Singletary", "Jack Lambert", "Dick Butkus", "Ray Lewis", "Lawrence Taylor"]
greatestLinebackers2.sort()
print(greatestLinebackers2)


# Reverse Function:
# modifies the list in place, meaning it changes the original list directly and does not return a new list.
greatestLinebackers2 = ["Mike Singletary", "Jack Lambert", "Dick Butkus", "Ray Lewis", "Lawrence Taylor"]
greatestLinebackers2.reverse()
print(greatestLinebackers2)


# Copy Function
#returns a copy of the specified list.
greatestForwards = ["Lebron James", "Larry Bird", "Julius Irving", "Dennis Rodman", "Elgin Baylor"]
greatestForwards1 = greatestForwards.copy()




# Tuples
# ordered, immutable sequences of items.
# they are similar to lists but cannot be changed after creation.

# tuple example - coordinates (1):
coordinates = (4, 5)
print(coordinates[0]) # 4

# tuple example - coordinates (2):
coord1 = (5, 9)
print(coord1[0]) # 5

# tuple example - multiple items of different types:
my_tuple = ("apple", 10, True, 3.14)


# Function:

# general greeting:
def say_hi(name, age):
    print("Hello " + name + ", you are " + str(age))

say_hi("Mike", "35")
say_hi("Steve", "70")

print("\n")


# greeting - new employee:
def new_hire(name, department):
    print("Welcome " + name + ", Department of " + str(department))
    
new_hire("John Smith", "Energy")
new_hire("Kwame Igbo", "Engineering")
new_hire("Nancy Stedson", "Accounting")
new_hire("Luna Ng", "Operations")




# Return Statement:
# exiting the function: execution immediately terminates, and conrtrol is passed back to the point where the the function was called.
# returning a value: can optionally be followeed by an expression or a value. Thsi vcalue is then passed back to the calling code and can be assigned to a variable or used directly in an expression.


# Function - cube element:
# cube a number to the power of three.
def cube(num):
    return num*num*num 


# cube(3)
result = cube(4)
print(result) # result = 64



# If Statement:
# used for conditional execution, allowing a block of code
# to run only if a specified condition evaluates to True.
I wake up
If I'm hungry
    I eat breakfast
    
I leave my house
if it's cloudy
    I bring my umbrella
otherwise
    I bring sunglasses
    
I'm at a restaurant
if I want meat
    I order steak
otherwise if I want pasta
    I order spaghetti & meatballs
otherwise
    I order a salad.
    

# boolean variable:
# and statement: logical operator used to combine conditional expressions.
    # it evaluates to True only if all the conditions it connects are True.
    # if even one of the conditions is False, the entire and expressions evaluates to False.
# or statement: used to combine conditional expressions.
    # it evaluates to True if at least one of the conditions it connects is True.
# elif: else if and is used in conditional statement to chack multiple conditions sequentially after an initial if statement.
is_male = True
is_tall = True

if is_male or is_tall:
    print("You are a male or tall or both")
elif is_male and not(is_tall):
    print("You are a short male")
elif not(is_male) and not(is_tall):
else:
    print("You are neither male nor tall")


print("\n")


# My Example - Good and Bad Student
goodStudent = True

if goodStudent:
    print("You are a good student!")
else:
    print("You are a bad student!")

print("\n")


# My Example - Basketball Player (left/right handed)
bball_player = True
left_handed = True 

if bball_player and left_handed:
    print("You are a left-handed basketball player. Nice!")
elif bball_player and not(left_handed):
    print("Boo! Right handed basketball players are sooo common!")

print("\n")




# If Statements and Comparisons:
# used to compare two values and return a Boolean result.
    # returns True or False.

# create a function and print out the biggest number:
def max_num(num1, num2, num3):
    if num1 >= num2 and num1 >= num3:
        return num1
    elif num2 >= num1 and num2 >= num3:
        return num2
    else:
        return num3


# My Example - Top Scorer (copilot):
# f-string: formatted string literals
    # provides a concise and readable way to embed expressions inside string literals.
    # Python 3.6: they are now the preferred method for string formatting.
def top_scorer(player1_name, player1_points, player2_name, player2_points, player3_name, player3_points):
    if player1_points >= player2_points and player1_points >= player3_points:
        return f"{player1_name} is the top scorer with {player1_points} points."
    elif player2_points >= player1_points and player2_points >= player3_points:
        return f"{player2_name} is the top scorer with {player2_points} points."
    else:
        return f"{player3_name} is the top scorer with {player3_points} points."


# My Example - NBA Top Scorer (copilot)
print(top_scorer("Jordan", 32, "Kobe", 28, "LeBron", 35))
# Output: LeBron is the top scorer with 35 points.


# My Example - Highest Scorers
def highest_score(score1, score2, score3):
    if score1 >= score2 and score1 >= score3:
        return score1
    elif score2 >= score1 and score2 >= score3:
    else:
        return score3

print(highest_score(22, 30, 28))    # Output: 30




# Building A Better Calculator
# perform all the basic arithmetic.
# enter a number, operator, and the second number and the operation for them.
    # shows how we can use if statements in a practical application.


# retrieving first number (num1):
# retrieving operator (op):
# retrieving second number (num2):
num1 = float(input("Enter number: "))
op = input("Enter operator: ")
num2 = float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-"
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Number")




# Dictionaries
# unordered, changeable collections of data items that store values in key velue pairs.
    # Each key within a dictionary must be unique and immutable (strings/numbers/tuples) with the associated values can be of any data type.
    # Key Value Pairs - a data structure where a uniquer "key" is a associates with a value, much like a word (key) in a dictionary is associates with its definition (value).
monthConversions = {
    "Jan": "January",
    "Feb": "Feburary",
    "Mar" : "March",
    "Apr" : "April",
    "May" : "May",
    "Jun" : "June",
    "Jul" : "July",
    "Aug" : "August",
    "Sep" : "September",
    "Oct" : "October",
    "Nov" : "November",
    "Dec" : "December",
}

print(monthConversions["Mar"])

print(monthConversions.get("Dec")) #method returns the value of the item with the specified key.


# Get Method - Syntax Example
# Key Value Pairs = unordered collections of mutable data.
    # Each item is dictionary is a key value pair, where a unique key maps to specific value.
# Keep in mind that youll be using key value pairs all the time to store and retrieve data in Python.
car = {
    "brand": "Ford",
    "model": "Mustang",
    "year": 1964
}

x = car.get("price", 15000)

print(x)




# While Loops
# repeatedly executes a block of code as long as a specified condition remains True.
i = 1
while i < 10:
    # code inside the while loop.
    # code will continually run.
    print(i)
    i += 1

print("Done with loop!")




# Building A Game
# prompt the user for words.
secret_Word = "giraffe"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != secret_word and not(out_of_guesses):
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else: 
        out_of_guesses = True

print("You win!")




# For Loop - FCC Example
# used for iterating over a sequence (such as a list, tuple, string, or range) or other iterable objects.
# Allows you to execute a block of code repeatedly, once for each item in the sequence.
# letter is the variable.
# "giraffe academy" is the string.
# we are basically looping thru the entire string.
for letter in "Giraffe Academy":
    print(letter)


# For Loop - looping thru an array
friends = ["Jim", "Karen", "Kevin"]
print(friend)


# For Loop - looping from 1 to 10.
for index in range(10):
    print(index)


# For Loop - running thru first iteration of the loop.
for index in range(5):
    if index == 0:
        print("First Iteration")
    else:
        print("Not first")

for index in range(lens(friends)):
    print(index[index]) # access each friend in the list.
# this will give me a range between zero and the number of friends in my array list. 


# For Loop - Example - NBA Top Scorers
top_scorers = ["Shai Gilgeous-Alexander", "Luka Dončić", "Giannis Antetokounmpo", "Nikola Jokić", "Stephen Curry"]

# this will output each player's name on a new line.
for player in top_scorers:
print(player)




# Exponent Function
# operation of raising a base number to a given power (exponent).
# using the ':' operator: **
# Exponent Function - Simple Math
print(2**3)


# Exponent Function - Complex Function
def raise_to_power(base_num, pow_num): 
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(2, 3))


# Exponent Function - My Example
def raise_to_power(base_num, pow_num): 
    result = 1
    for index in range(pow_num):
        result = result * base_num
    return result

print(raise_to_power(100, 20)) # 2000000000000+




# 2d Lists and Nested Loops
# 2D Lists = a list where each element is itself anothet list. 
    # The structure allows for the representation of data in a tbaulat or grid like format, similiar to a matric or a spreadsheet.
# Nested Loops = involve placing one loop inside the body of another loop. 
    # This structure allows for repeated actions within another set of repeated actions.
# Both for loops and while loops can be nested.

# 2D List - Access Elements
# create list - number one thru nine.
# print out the number 1, located at 0-0.
# loop thru the list and print out the entire list.
number_grid = [ 
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print(number_grid[0][0])

for row in number_grid:
    for col in row:j
    print(row)




# 2D List - My Example
baseball_team = [ 
    ["Pitcher", "Catcher", "First Base"], 
    ["Second Base", "Shortstop", "Left Field"],
    ["Center Field", "Right Field"]
]

print(baseball_team[0][0]) # Catcher
print(baseball_team[3][1]) # Right Field




# Sport Slang Translator
# we will create a function that takes a phrase and replaces certain letters or words with NBA or soccer-inspired terms.
# Concepts Reinforced:
    # Function: sports_translate() processes the input.
    # Loop: for word in phrase.split() loops through each word.
    # Conditionals: if/elif/else checks for matches and replaces them.
    # String Manipulation: .split() and .strip() help clean and format the output.
# example = "ball" -> "b[soccer icon]ll"
# example = "run" -> "fast break"

def sports_translate(phrase):
    translation = ""
    for word in phrase.split():
        if word.lower() == "ball":
            translation += "b⚽ll "
        elif word.lower() == "run":
            translation += "fast break "
        elif word.lower() == "goal":
            translation += "GOOOOOAL! "
        elif word.lower() == "jump":
            translation += "slam dunk "
        else:
            translation += word + " "
    return translation.strip()

# Ask user for input
user_input = input("Enter a sports-related phrase: ")
print(sports_translate(user_input))


# Want To Level It Up:
# replace letter with emojis.
# add player names or team references.
# make it case sensitive or preserve punctuation.
# create a reverse translator to decode it back.
