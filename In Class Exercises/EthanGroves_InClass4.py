#########################################################################
#########################################################################
########                                                         ########
########                   Inclass4 Part 2                       ########
########                                                         ########
#########################################################################
#########################################################################

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

# Prints the string "I will now count my chickens:"
print "I will now count my chickens:"

# Prints the string "Hens 30"
print "Hens", 25 + 30 / 6
# Prints the string "Roosters 97"
print "Roosters", 100 - 25 * 3 % 4

# Prints the string "Now I will count the eggs:"
print "Now I will count the eggs:"

# Prints the integer "7"
print 3 + 2 + 1 - 5 + 4 % 2 - 1 / 4 + 6

# Prints the string "Is it true that 3 + 2 < 5 - 7?"
print "Is it true that 3 + 2 < 5 - 7?"

# Prints the string "False"
print 3 + 2 < 5 - 7

# Prints the string "What is 3 + 2? 5"
print "What is 3 + 2?", 3 + 2
# Prints the string "What is 5 - 7? -2"
print "What is 5 - 7?", 5 - 7

# Prints the string "Oh, that's why it's False."
print "Oh, that's why it's False."

# Prints the string "How about some more."
print "How about some more."

# Prints the string "Is it greater? True"
print "Is it greater?", 5 > -2
# Prints the string "Is it greater or equal? True"
print "Is it greater or equal?", 5 >= -2
# Prints the string "Is it less or equal? False"
print "Is it less or equal?", 5 <= -2

#PART II

# Sets the variable, days, equal to the string "Mon Tue Wed Thu Fri Sat Sun"
days = "Mon Tue Wed Thu Fri Sat Sun"
# Sets the variable, months equal to the string below:
"""
Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
"""
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"

# Prints the string "Here are the days: Mon Tue Wed Thu Fri Sat Sun"
print "Here are the days: ", days
# Prints the string shown below:
"""
Here are the months:  Jan
Feb
Mar
Apr
May
Jun
Jul
Aug
"""
print "Here are the months: ", months

#PART III

# Creates a list of length 5 with the digits 1-5
the_count = [1, 2, 3, 4, 5]
# Creates a list of length 4 with the strings 'apples', 'oranges', 'pears', 'apricots'
fruits = ['apples', 'oranges', 'pears', 'apricots']
# Creates a mixed list of integers and strings with the values:
# 1, 'pennies', 2, 'dimes', 3, 'quarters'
change = [1, 'pennies', 2, 'dimes', 3, 'quarters']

# A for loop that prints out all the values of the list: the_count
# The print statements have the following form: "This is count #"
for number in the_count:
    print "This is count %d" % number

# A for loop that prints out all the values of the list: fruits
# The print statements have the following form: "A fruit of type: string"
for fruit in fruits:
    print "A fruit of type: %s" % fruit

# A for loop that prints out all the values of the list: change
# The print statements have the following form: "I got 'value'"
# Use %r format when you don't know
#if the elements are strings or integers
for i in change:
    print "I got %r" % i

# Creates an empty list
# we can also build lists, first start with an empty one
elements = []

# A for loop that prints a value and adds the new value to the list: elements
# The print statements have the following form: "Adding # to the list."
# then use the range function to do 0 to 5 counts
for i in range(0, 6):
    print "Adding %d to the list." % i
    # append is a function that lists understand
    elements.append(i)

# A for loop that prints out all the values of the list: elements
# The print statements have the following form: "Element was: #"
for i in elements:
    print "Element was: %d" % i

#########################################################################
#########################################################################
########                                                         ########
########                   Inclass4 Part 3                       ########
########                                                         ########
#########################################################################
#########################################################################

"""What does the code below do? Run the code in iPython.
For each line of code, add an explanation
through a comment."""

#PART I

#Use the code from Lecture14.py to create and change the 
#'stuff' list; Then comment on each line of the code below
#what it does, and what the result is

ten_things = "Apples, Oranges, Crows, Telephone, Light, Sugar"
stuff = ten_things.split(', ')

# Prints out the second element in the list: stuff
print stuff[1]
# Prints out the last element in the list: stuff
print stuff[-1] 
# Prints out the last element in the list: stuff
print stuff.pop()
# Prints out every element in the list, seperated by a space
print ' '.join(stuff)
# Prints out the 4th and 5th elements, seperated by the # sign
print '#'.join(stuff[3:5]) 

#PART II

#Create comments where marked with # to explain the code below

# Creates a dictionary with five key:value pairs, where each key is the name of a state
# and each value is the abbreviation for the given state.
states = {
    'Oregon': 'OR',
    'Florida': 'FL',
    'California': 'CA',
    'New York': 'NY',
    'Michigan': 'MI'
}

# Creates a dictionary with three key:value pairs, where each key is the abbreviation of a state
# and each value is the name of a city within the given state.
cities = {
    'CA': 'San Francisco',
    'MI': 'Detroit',
    'FL': 'Jacksonville'
}

# Adds two new key:value pairs to the dictionary 'cities' following the same procedure described above.
cities['NY'] = 'New York'
cities['OR'] = 'Portland'

# Prints 10 '-' characters, then prints the two values for the keys: 'NY' and 'OR'
# in the cities dictionary in the format shown below:
'''
----------
NY State has:  New York
OR State has:  Portland
'''
print '-' * 10
print "NY State has: ", cities['NY']
print "OR State has: ", cities['OR']

# Prints 10 '-' characters, then prints the two values for the keys: 'Michigan' and 'Florida'
# in the states dictionary in the format shown below:
'''
----------
Michigan's abbreviation is:  MI
Florida's abbreviation is:  FL
'''
print '-' * 10
print "Michigan's abbreviation is: ", states['Michigan']
print "Florida's abbreviation is: ", states['Florida']

# Prints 10 '-' characters, then takes the two values for the keys: 'Michigan' and 'Florida'
# in the states dictionary and uses those values as keys to get and print the values 
# from the cities dictionary in the format shown below:
'''
----------
Michigan has:  Detroit
Florida has:  Jacksonville
'''
print '-' * 10
print "Michigan has: ", cities[states['Michigan']]
print "Florida has: ", cities[states['Florida']]

# Prints 10 '-' characters, then prints out each value in the dictionary states
# in the format shown below:
'''
----------
California is abbreviated CA
Michigan is abbreviated MI
New York is abbreviated NY
Florida is abbreviated FL
Oregon is abbreviated OR
'''
print '-' * 10
for state, abbrev in states.items():
    print "%s is abbreviated %s" % (state, abbrev)

# Prints 10 '-' characters, then prints out each value in the dictionary cities
# in the format shown below:
'''
----------
FL has the city Jacksonville
CA has the city San Francisco
MI has the city Detroit
OR has the city Portland
NY has the city New York
'''
print '-' * 10
for abbrev, city in cities.items():
    print "%s has the city %s" % (abbrev, city)

# Prints 10 '-' characters, then prints out each value for both dictionaries cities and states
# in the format shown below:
'''
----------
California state is abbreviated CA and has city San Francisco
Michigan state is abbreviated MI and has city Detroit
New York state is abbreviated NY and has city New York
Florida state is abbreviated FL and has city Jacksonville
Oregon state is abbreviated OR and has city Portland
'''
print '-' * 10
for state, abbrev in states.items():
    print "%s state is abbreviated %s and has city %s" % (
        state, abbrev, cities[abbrev])
