print("Input first number", end=' ')
x = int(input())

print("Input second number", end=' ')
y = int(input())

print("Select math operator. +, -, *, /.")
o = input()

if o == "+":
    print(x+y)
elif o == '-':
    print(x-y)
elif o == '*':
    print(x*y)
elif o == '/':
    print(x/y)
else:
    print("Operator not supported.")
