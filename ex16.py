from sys import argv

script, filename = argv

print(f"We're going to erase {filename}.")
print("If you don't want that, hit CTRL-C (^C)>")
print("If you want to do that hit RETURN.")

input("?")

print("Opening the file...")
target = open(filename, 'w')

print("truncating the file. GoodBye!")
target.truncate()

print("Now I'm going to ask you for three lines.")

line1 = input("line 1: ")
line2 = input("line 2: ")
line3 = input("line 3: ")

print("I'm going to write these to the file.")

ftxt = f"{line1} \n{line2} \n{line3} \n"
target.write(ftxt)

print("And finally we close it")
target.close()
