# # Module
# import math
# num = int(input('Enter number to find out square root: '))
# print(f'Square root of {num} \t', round(math.sqrt(num),2))


# #--------------------------------
# # Inspect Module
# import math
# import inspect

# functions = inspect.getmembers(math, inspect.isbuiltin)

# print('All functions in Math module')
# for n, func in functions:
#     print(n, end="\t")

# #--------------------------------
# # Random Number Pic

# import random
# print('Random number from 1 to 1000')

# print(random.randint(1,1000))

# #--------------------------------
# # Lucky Draw

# import random
# name=input('Enter name: ')
# luckyNumber = random.randint(1,10)
# print(f'Welcome Mr.\\Ms {name} Coupon Number: {luckyNumber}')
# if (luckyNumber==1):
#     print('you have won Proton XL-65 Car')
# elif(luckyNumber==3):
#     print('you have won a IPad')
# elif(luckyNumber==9):
#     print('you have won a IPhone')
# else:
#     print('Better Luck Next Time')

#--------------------------------


# import datetime
# import inspect
# dtclassess = inspect.getmembers (datetime, inspect.isclass)

# print('All Classes in datetime module')
# for n, func in dtclassess:
#     print(n,end="\t")

# print('\n ---Today---\n')
# print(datetime.date.today())

# print('\n ---Time---\n')
# print(datetime.datetime.now().time())


# cttime = datetime.datetime.now().time()
# formattedtime = datetime.datetime.now().strftime('%I %M %S %p')

# print('Current time', cttime)
# print('Formatted time',formattedtime)

#--------------------------------

# import inspect

# functions = inspect.getmembers(os, inspect.isbuiltin)


# print('All functions in OS module')
# for n, func in functions:
#     print(n, end="\t")

#--------------------------------

# import os
# print ('Current Directory: ',os.getcwd())

#--------------------------------
# Create a folder inside current directory using python

# import os
# cdir = os.getcwd()
# folder_name = input('Enter folder name to create : \t')
# folder_path = os.path.join(cdir, folder_name)

# if(os.path.exists(folder_path)):
#     print('Folder already exist')
# else:
#     os.makedirs(folder_path, exist_ok=True)
#     print(f'{folder_name} created at {folder_path}')

#--------------------------------
# import os           #CGPT

# # Rename a folder Exercise
# # write code to rename a folder
# # you will take folderName from user
# # if it is exist you will ask new name and rename it

# folder_name = input("Enter the folder name to rename: ")

# if os.path.exists(folder_name):
#     # Rename the folder to a temporary name first
#     os.rename(folder_name, "renamed_folder")

#     # Ask for a new name
#     new_name = input("Enter the new folder name: ")

#     # Rename the temporary folder to the new name
#     os.rename("renamed_folder", new_name)

#     print(f'Folder "{folder_name}" has been renamed to "{new_name}".')

# else:
#     print(f'Folder "{folder_name}" does not exist!')

#--------------------------------
# Will be imported to ex5.py
import random

def findwinner():
    name=input('Enter Your name: ')
    luckyNumber=random.randint(1,10)
    print(f'Welcome Mr./Ms {name}, Coupon Number: {luckyNumber}')
    if(luckyNumber==1):
        print('you have won Proton LX-65 Car')
    elif(luckyNumber==3):
        print('you have won a IPad')
    elif(luckyNumber==9):
        print('you have won an IPhone')
    else:
        print('Better Luck Next Time')