
# username=input("Enter User Name: ")
# age=int(input("Enter age: "))
# salary=float(input("Enter Salary: "))
# databaseKn=input("Do you know database? (yes/no):").strip().lower() =="yes"
# print("Name:",username)   # .strip() makes your program forgiving — it ignores those extra spaces.
# print("Your age is",age)   # .lower() Converts the input to lowercase, doesn’t matter upper/lowercase
# print ("Salary is:",salary)
# print("Know the database?",databaseKn)

# # Adding Two Numbers
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1+num2
# print(f"Result after adding {num1} and {num2} = \t {result}")

# # Multiply Two Numbers
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1*num2
# print(f"Result after multiplication {num1} and {num2} = \t {result}")

# # % Finding Remainder Numbers
# num1=int(input("First Number: \t"))
# num2=int(input("Second Number: \t"))
# result=num1%num2
# print(f"Remainder after Dividing {num1} by {num2} = \t {result}")

# taking more than one input using single line
num1,num2=input("Enter two numbers separated by space ").split()
result=int(num1)+int(num2)
print(f"Numbers you have entered are {num1} and {num2}, the total addition of the two numbers is {result}")