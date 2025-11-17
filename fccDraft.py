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


# define a translate function.
# phrase will be our piece of information that we want to translate.
    # any vowels become g's.
# we want to loop thru every vowel in this phrase and change it to g.
# if its not a vowel we'll leave it alone.
# "AEIOU" will be our phrase we will be checking.
def translate(phrase):
    translation = ""
    for letter in phrase:
        if letter in "AEIOUaeiou":
            translation = translation + "G"
        else: 
            translation = translation + "g"
    return translation

# allow user to input information.
# pass whatever the user inputs.
# we are essentially combining these statements together.
print(translate(input("Enter a phrase: ")))




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




# Comments
# comments are used to add explanatory notes within the code.
    # comments are ignored by the interpreter during executiion. They serve to improve code readibility and maintability.


# Single Line Comment:
# this is a comment!


# Multiple Line Comment:
# this is a ...
# multi line comment.


# Triple Quoted Strings (Docstrings):
def nvda_function(price):
    """
    This function takes a price value (like opening or closing price) and prints a message with that value.
    """
    print(f"The NVDA price you entered is: ${price}")



# Try/Except
# used for handling exceptions (errors) that might occur during the execution of a program.
# this mechanism allows for graceful error handling, preventing the program from crashing and prpvoding alternative actions or informative messages when an error arises.


# Error Handling - Part 1
# prompt the user to enter an input command.
# then convert that to an integer.
# this example will throw an error:
    # ValueError: invalid literal for int() with base 10: 'asdref'
number = int(input("Enter a number: "))
print(number) 


# Error Handling - Part 2
# here we will use try/except blocks
try:
    number = int(input("Enter a number: "))
    print(number) 
except ZeroDivisionError: 
        print("Divide by zero")
except ValueError:
    print("Invalid Input")


# Basic Structure - Google
try:
    # Code that might raise an exception
    # For example:
    result = 10/0
except ZeroDivisionError:
    # Code to execute if a ZeroDivisionError occurs
    print("Error: Cannot divide by zero!")


# Reading Files:
# To read a file in Python, the open() function is used to establish a connection to the file, and then methods like read(), readline(), or readlines() are employed to retrieve its content.
# The with open(...) as f: statement is rec'd and safest way to handle file operations, as its automatically ensures the files is closed, even if errors occur.


# Sample Text File - read the file.
Jim - Salesman
Dwight - Salesman
Pam - Receptionist
Michael - Manager
Oscar - Accountant


# "r" = read
# "w" = write
# "a" = append (add new information).
# "r+" = read and write privileges.
employee_file = open("employees.txt", "r")


# close the file so we no longer have access to it.
employee_file.close()


# returns a boolean value - yes or no.
print(employee_file.readable())


# prints out entire contents in the file.
print(employee_file.read())


# prints out the first TWO lines of the file.
print(employee_file.readline())
print(employee_file.readline())
employee_file.close()


# prints out the first few lines of the file and places them into a an array.
employee_file.readlines())
employee_file.close()


# loops thru the entire file and prints out each line of the file.
employee_file = open("employees.txt", "r")
for employee in employee_file.readlines():
    print(employee)
employee_file.close()


# close the file so we no longer have access to it.
employee_file.close()


# close the file so we no longer have access to it.
employee_file.close()


# append or add another employee to the file:
# you can use an escape character "\n" to the have the appended item placed on the new line.
employee_file = open("employees.txt", "a")
employee_file.write("Toby - Human Resources")
employee_file.close()


# write or replace a file:
# you can also create a html, css, or webpage.
employee_file = open("employees1.txt", "w")
employee_file.write("\nKelly - Customer Service")
employee_file.close()


# Starting Five

def get_cavs_roster():
    # Starting Five
    starting_five = [
        {"name": "Lonzo Ball", "number": 2},
        {"name": "Donovan Mitchell", "number": 45},
        {"name": "De’Andre Hunter", "number": 12},
        {"name": "Evan Mobley", "number": 4},
        {"name": "Jarrett Allen", "number": 31}
    ]

    # Bench Players
    bench_players = [
        {"name": "Darius Garland", "number": 10},
        {"name": "Thomas Bryant", "number": 3},
        {"name": "Tyrese Proctor", "number": 24},
        {"name": "Nae’Qwan Tomlin", "number": 30},
        {"name": "Sam Merrill", "number": 5},
        {"name": "Craig Porter Jr.", "number": 9},
        {"name": "Jaylon Tyson", "number": 20},
        {"name": "Larry Nance Jr.", "number": 22},
        {"name": "Dean Wade", "number": 32},
        {"name": "Luke Travers", "number": 8},
        {"name": "Chris Livingston", "number": 7},
        {"name": "Max Strus", "number": 1}
    ]

    # Append bench to starting five
    full_roster = starting_five + bench_players
    return full_roster


# Example usage:
cavs_roster = get_cavs_roster()
for player in cavs_roster:
    print(f"{player['name']} — #{player['number']}")




# Modules and Pip
# a module is a file containing Python definitions and statements.
    # modules allow you to logically organize your Python into reusable units, promoting modular programming and code reusability.
# pip is a package manager written in Python and is used to install and manage software packagaes.
    # pip connects to an online software repository of public packages, names the Python Package index.


# Learn Python - Sample Porgram
# file name is UsefulTools.py
import random

# 1) variable with feet into miles.
# 2) variable with meters into kilometers.
# 3) variable with Beatles members.
feet_in_mile = 5280
meters_in_kilometer = 1000
beatles = ["John Lennon", "Paul Harrison", "Ringo Star"]


# function that tells you the file extension of a particular file.
def get_file_ext(filename):
    return filename[filename.index(".") + 1:]


# function which simulates rolling dice. 
def roll_dice(num):
    return random.randint(1, num)


# instead of copying/pasting the things we need into another file...
# we can just import the contents of a file or the entire file using the import statement.
import useful_tools

print(useful_tools.roll_dice(10))


# Python Module Index = https://docs.python.org/3/py-modindex.html
# Python Docx = https://docs.python.org/3/py-modindex.html

# checking if pip is installed on your terminal:
# Linux: pip --version
# Linux: pip install python-docx

# package will be installed in the "Lib" folder inside VS Code.




# Classes and Objects
# class = serves as a blueprint for creating objects. it encapsulates data (attributes) and functionality (methods) into a single, cohesive unit.
# objects = fundamental building block of data. Essentially, all data in a Python program is represented by objects, including numbers, strings, lists, functions, and even classes themselves.

# create a class for a student
# student.py file
# we can use strings, integers, and booleans to map out what a student should be:
class Student:
    def __init___(self, name, major, gpa, is_on_probation):
        self.name = name
        self.major = major
        self.gpa = gpa
        self.is_on_probation = is_on_probation


# create new app.py file
# we can model real word objects and create data types.
from Student    # reference: Student.py file
import Student  # reference: Student class

student1 = Student("Jim", "Business", 3.1, False)
student2 = Student("Pam", "Art", 2.5, True)
print(student1.name)
print(student2.major)




# Build A Multiple Choice Quiz
# classes, if statements, loops, etc.
# whats being asked + what the answer is.

from Questions import Question.py

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Purple\n(c) Orange\n\n",
    "What color are Bananas?\n(a) Teal\n(b) Magenta\n(c) Yellow\n\n",
    "What color are strawberries?\n(a) Yellow\n(b) Red\n(c) Blue\n\n"
]


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "c"),
    Question(question_prompts[2], "b"),
]


# ask question and store their response in a variable.
def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
        score += 1  #adding one to the score.
    print("You got " + str(score) + "/" + str(len(questions)) + "Correct!")

          
run_test(questions)


# File: Question.py
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer

# Conclusion
# How It Works:
    # Store The Prompts:
        # A list called "question_prompts" holds all the text for each multiple choice question. Each string includes the question itself and the possible answer choices.
    # Ceate "Question" Objects:
        # Each question is represented by a Question object, which stores both the prompt and the correct answer. This makes it easy to manage questions as reusable objects.
    # Build The Quiz List:
        # The "questions" list collects all the Questions objects. This list is what the promgram loops throubgh when running the quiz, ensuring each question is asked in order.
    # Run The Test Loop:
        # The run_test function iterates over the list of questions. For each one, it displays the prompt, waits for the user's input, and checks whether the response matches the correct answer.
    # Calculate And Display The Score
        # every time the user answers correctly, the score increases by one. At the end of the loop, the program prints the total score alongside the number of questions, giving the user a clear result.
###This breakdown shows how your quiz flows from question storage -> object creation -> looping through questions -> checking answers -> final score output.


# Cleveland Sports Trivia Quiz 
# How This Works
    # Each trivia question is stored in question_prompts with numbered choices.
    # The questions list pairs each prompt with the correct answer(as "1", "2", or "3").
    # The "run_test" function loops through each question, asks the user for input, and checks correctness.
    # At the end, rhe program prints the total score out of the number of questions.


# File: main.py
from Question import Question

# Prompts for each question
question_prompts = [
    "What color are the Cleveland Browns jerseys?\n"
    "1) Pink and Teal\n"
    "2) Green and White\n"
    "3) Brown and Orange\n\n",

    "When were the Indians (Blues/Guardians) founded?\n"
    "1) 2025\n"
    "2) 1968\n"
    "3) 1901\n\n",

    "Who is the Cavs all-time leader in points scored?\n"
    "1) Zydrunas Ilgauskas\n"
    "2) LeBron James\n"
    "3) Daniel 'Booby' Gibson\n\n"
]

# Correct answers: Browns = 3, Guardians founded = 3, Cavs leader = 2
questions = [
    Question(question_prompts[0], "3"),
    Question(question_prompts[1], "3"),
    Question(question_prompts[2], "2"),
]

def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + "/" + str(len(questions)) + " Correct!")

run_test(questions)


# File: Question.py
class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer



# App.py file
from Student import Student 

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())


# Student.py file - Accompanying file.
class Student:
    def __init__(Self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


# define a function determining whether a student is/isnt on honor roll:
# provides a service to the object of this class (Student):
def on_honor_roll(Self):
    if self.gpa >= 3.5:
        return True
    else:
        return False


# Inheritance
# allows a new class (child class or derived class) to inherit attributes and methods fro man exisiting class (parent class or base class).
    # This mechanism promotes code reusability and establishes a herarchhical "is-a" relationship between classes.


# App.py file
from Student import Student 

student1 = Student("Oscar", "Accounting", 3.1)
student2 = Student("Phyllis", "Business", 3.8)

print(student1.on_honor_roll())


# Student.py file - Accompanying file.
class Student:
    def __init__(Self, name, major, gpa):
        self.name = name
        self.major = major
        self.gpa = gpa


# define a function determining whether a student is/isnt on honor roll:
# provides a service to the object of this class (Student):
def on_honor_roll(Self):
    if self.gpa >= 3.5:
        return True
    else:
        return False


# Inheritance
# allows a new class (child class or derived class) to inherit attributes and methods fro man exisiting class (parent class or base class).
    # This mechanism promotes code reusability and establishes a herarchhical "is-a" relationship between classes.


# Chef.py file
# The chef makes three distinct dishes.
class Chef:

    def make_chicken(self):
        print("The chef makes a chicken.")

    def make_salas(self):
        print("The chef makes a salad.")

    def make_special_dish(self):
        print("The chef makes BBQ ribs.")




#App.py file 
# importing Chef.py file
from Chef import Chef

myChef() = Chef()


#Run file:
# Output: The chef makes BBQ ribs.
from Chef import Chef

myChef = Chef()
myChef.make_special_dish()


# I want to create a class that models a Chinese chef.
# ChineseChef.py file:
class ChineseChef:

class Chef:

    def make_chicken(self):
        print("The chef makes a chicken.")

    def make_salas(self):
        print("The chef makes a salad.")

    def make_special_dish(self):
        print("The chef makes orange chicken.")

    def make_friend_rice(self):
        print("The chef makes fried rice.")


#App.py file:
# importing ChineseChef.file:
from Chef import Chef
from ChineseChef import ChineseChef

myChef = Chef()
myChef.make_special_dish()

myChineseChef = ChineseChef()
myChineseChef.make_special_dish()


# now we use inheritance:
# inside of this Chinese Chef, I want to be to use all of the functions within the Chef class.
from Chef import Chef

class ChineseChef(Chef):
    def make_fried_rise(self):
        print("The chef makes friend rice.")


