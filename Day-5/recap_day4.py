def display():
            print('Welcome to recap of Functions')

def welcome(name):
        print('Welcome to Functions Mr.\\Ms.',name)

def cube(num):
        cube_num=num*num*num
        print(f'Cube of given number: {num} is =\t {cube_num}')

def square(num):
        return num*num


# welcome('Abu')
# display()
# my_num=int(input('Enter number to find out cube:\t'))
# cube(my_num)
# username=input('Enter User Name: \t')
# my_num=int(input('Enter number to find out cube and square: \t'))
# welcome (username)
# cube(my_num)
# sq=square(my_num)
# print(f'Square of {my_num} is: {sq}')
# print(f'Number: {my_num} Square: {sq}')
#---------------------
# def salBonus (salary):
#         return salary*0.10
# my_sal=float(input('Enter Salary to find out bonus: \t'))
# bonus=salBonus (my_sal)
# print(f'Salary {my_sal} Bonus: {bonus}')
# print(f'Salary after bonus =\t', (my_sal+bonus))
#--------------------
def salBonus (salary):
        bonus=salary*0.10                                 #no Return-unable salary+bonus
        print(f'Salary {salary} Bonus: {bonus}')

my_sal=float(input('Enter Salary to find out bonus: \t'))
salBonus(my_sal)
