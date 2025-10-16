# 1️⃣ Exception Handling (Safety Net)

def safe_divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        print("Cannot divide by zero!")
        return None

print(safe_divide(10, 2))  # 5.0
print(safe_divide(10, 0))  # Cannot divide by zero! None

#=======================================
# 2️⃣ Files (Store / Read Data)

# Write to a file:
with open("data.txt", "w") as file:
    file.write("Hello, Haidar!\nPython is fun!")

# Read from a file:
with open("data.txt", "r") as file:
    print(file.read())

# 🟢 Output:

# Hello, Haidar!
# Python is fun!

#=======================================
# 3️⃣ Module (Reusable Code)

# File: mymodule.py

def greet(name):
    print(f"Hello, {name}!")

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    
    def introduce(self):
        print(f"My name is {self.name}, I'm {self.age} years old.")

#=======================================
# 4️⃣ Package (Folder of Modules)

# Folder: mypackage/

mypackage/
    __init__.py
    mymodule.py

# Use in main program:

from mypackage.mymodule import greet, Person

greet("Haidar")         # Function from module
p1 = Person("Haidar", 9) # Class from module
p1.introduce()          # Call method

# 🟢 Output:

# Hello, Haidar
# My name is Haidar, I'm 9 years old.

#=======================================
# 5️⃣ Combine File + Exception + Module

def read_file_safe(filename):
    try:
        with open(filename, "r") as f:
            return f.read()
    except FileNotFoundError:
        print(f"Error: {filename} not found!")
        return None

content = read_file_safe("data.txt")
print(content)

content2 = read_file_safe("not_exist.txt")  # File missing

# 🟢 Output:

# Hello, Haidar!
# Python is fun!
# Error: not_exist.txt not found!
# None

# 6️⃣ Quick Mental Map
# Exception → safety net
# File → store/retrieve data
# Module → reusable code (functions/classes)
# Package → folder of modules
# Class → blueprint inside module
# Function → action inside class or module
