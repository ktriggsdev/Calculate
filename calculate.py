welcome = '''
Welcome to Calculate 2.0
To begin please choose from the following:

a -> add()
s -> subtract()
m -> multiply()
d -> divide()
e -> exponent()
f -> floorDivision()
'''
print(welcome)

choice = input("Enter Your Choice: ")

choice = choice.lower()

def add():
    a = int(input("First number: "))
    b = int(input("Second Number: "))
    c = a + b
    return c

def subtract():
    a = int(input("First number: "))
    b = int(input("Second Number: "))
    c = a - b
    return c

def multiply():
    a = int(input("First number: "))
    b = int(input("Second Number: "))
    c = a * b
    return c

def divide():
    a = int(input("First number: "))
    b = int(input("Second Number: "))
    
    if a == 0 or b == 0:
        raise ZeroDivisionError("You cannot divide by zero")
    else:
        c = a / b
    return c

def exponent():
    a = int(input("First number: "))
    b = int(input("Second Number: "))
    c = a ** b
    return c

def floorDivision():
    a = float(input("First number: "))
    b = float(input("Second Number: "))
    if a == 0 or b == 0:
        raise ZeroDivisionError("You cannot divide by zero")
    else:
        c = a // b
    return c

if choice == 'a':
    print(add())
    
elif choice == 's':
    print(subtract())
    
elif choice == 'm':
    print(multiply())
    
elif choice == 'd':
    print(divide())
    
elif choice == 'e':
    print(exponent())
    
elif choice == 'f':
    print(floorDivision())