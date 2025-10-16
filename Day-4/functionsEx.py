# def function_name(parameters):
#     '''Docstring'''
#           statement(s)

#Function without parameter
# def welcome():
#     print("Welcome to Functions")
#     print("Our First Function")

# welcome()

# Function with a Parameter
# def welcome(name):
#     print("Welcome to funtions in python Mr.\\ Ms.",name)

# username=input('Enter your name:\t')
# #function call
# welcome(username)

# Function with a Parameter and Return
# def add(num1,num2):
#     return num1+num2

# fnum=int(input("Enter first number:\t"))
# snum=int(input("Enter second number:\t"))
# print(f'Result after adding {fnum} and {snum} is =\t',add(fnum,snum))

def add(num1,num2):
    return num1*num2
fnum=int(input("Enter first number:\t"))               #check
snum=int(input("Enter second number:\t"))
print(f'Result after multiply {fnum} and {snum} is =\t',multi(fnum,snum))