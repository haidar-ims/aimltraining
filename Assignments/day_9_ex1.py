# Write a program using functions to find greatest of three numbers entered by user

def greatest(a,b,c):
   return max(a,b,c)
num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))
print(f'The greatest between {num1},{num2} and {num3} is' , greatest(num1,num2,num3))