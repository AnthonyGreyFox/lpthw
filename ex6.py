type_of_people = 10 # assigns a value to this variable, in binary 10 = 2
x = f"There are {type_of_people} types of people."

binary = "binary" #assigns a string to this variable
do_not = "don't" #assigns a string to this variable
# this assiigns a string containing two other strings to the variable y
y = f"Those who know {binary} and those who {do_not}."

# These two lines print the variables x & y
print(x)
print(y)

#This line prints a string containing the variable x
print(f"I said: {x}")
#This line prints a string containing the variable y
print(f"I also said: '{y}'")

#This line assigned the False boolean value to the variable
hilarious = False
#Assigns a string to this variable
joke_evaluation = "Isn't that joke so funny?! {}"

#prints a both variables applying formatting to the second
print(joke_evaluation.format(hilarious))

#assigns strings to these variables
w = " This is the left side of..."
e = "a string with a right side."

#prints both variables combined, since these variables are strings the strings
# are combined
print(w + e)
