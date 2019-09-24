from sys import argv
#read the WYSS section for how to run this
script, first, second = argv

print(" your age is", first, "and your name is", second)
v1 = input('Is this correct? Y/N ')

if v1 == "Y":
        print("thank you for your private information.. ha ha ha")
else:
        print("Please start again")
