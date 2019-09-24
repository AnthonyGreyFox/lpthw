#defines the function cheese_and_crackers as a function which
# accepts two inputs.
def cheese_and_crackers(cheese_count , boxes_of_crackers):
    #These lines print various strings, using format to insert
    #the input into the string.
    print(f"You have {cheese_count} cheeses!")
    print(f"You have {boxes_of_crackers} boxes of crackers!")
    print("Man that's enough for a party")
    print("Get a blanket, \n")

#Prints a string, this line is not indented and so is not part of the
# function
print("we can just give the function numbers directly:")
#Calls the function with the inputs inside the paranthesis.
cheese_and_crackers(20, 30)

#Prints a string
print("Or we can use variables form our script:")
#Assigns a value to the variable "ammount_of_cheese and amount_of_crackers"
amount_of_cheese = 10
amount_of_crackers = 50

#Call the funtion using the variables defined on lines 20 & 21
cheese_and_crackers(amount_of_cheese, amount_of_crackers)

#prints the string below.
print("We can even do math inside too:")
#calls the function using two sums separated the by a comma as inputs.
cheese_and_crackers(10 + 25, 5+6)

#prints the below string
print("And we can combine the two, variables and Math:")
#calls the function with using a sum of a predefined variable and an
# integer as the inputs.
cheese_and_crackers(amount_of_cheese + 100, amount_of_crackers + 1000)
