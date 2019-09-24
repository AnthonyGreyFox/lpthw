#Imports argv from sys
from sys import argv

#assigns argv to the variable input_file
script, input_file = argv

#defines the function print_all, which acts on a variable f
def print_all(f):
    #reads the contents of f and then prints them when the function is run
    print(f.read())

#defines the function rewind which also acts on variable f.
def rewind(f):
    #uses the seek function to find the first byte of f when the funciton is run.
    f.seek(0)

#defines a function print_a_line, which takes  takes 2 inputs
# line_count and f.
def print_a_line(line_count, f):
    #scans the file until it finds the \n character
    #then prints the the next line?? when function is run
    print(line_count, f.readline())

#opens the input_file variable and sets the variable current_file equal to it.
current_file = open(input_file)

#prints the string
print("First let's print the whole file:\n")

#runs the print_all function with current_file as it's input
print_all(current_file)

#prints the string
print("Now let's rewind, kind of like a tape.")

#runs the rwind function with current_file as it's input
rewind(current_file)

#prints the string
print("Let's print three lines:")

#sets current_line equal to 1
current_line = 1
#runs function print_a_line, with the current_line and current_file as inputs
#this prints a line from the file, current_file is the file and
#current_line is the line in that file to print
print_a_line(current_line, current_file)

#takes the current value of the variable and adds 1 to it.
current_line = current_line + 1
#same as above, except now current_line is equal to 2 so it prints the
#second lines of the file
print_a_line(current_line, current_file)

#takes the current value of the variable and adds 1 to it.
current_line = current_line + 1
#same as above, except now current_line is equal to 3 so it prints the
#second lines of the file
print_a_line(current_line, current_file)
