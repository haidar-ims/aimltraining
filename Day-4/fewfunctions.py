# def factorial(num):
#     if((num==0)or(num==1)):
#         return 1
#     else:
#         return num*factorial(num-1)
    

# num=int(input('Enter a number to find out factorial: '))
# print(f'Factorial of {num} is:',factorial(num))

#Write a python function which converts inches to cms.
# 1inch = 2.5cm

# def inchToCm(inches):
#     return inches*2.5

# inches=float(input('Enter length in Inches:\t'))       

# print(f'{inches} inches is:{inchToCm(inches)} cm')
#-------------

#write a function to find out the table of given number
def gen_table(num):
    for i in range(1,11):
        print(f'{num}*{i}=\t{num*i}')

number=int(input('Enter number to find out table'))
gen_table(number)