# # Built-in Module

# import math
# my_num = int(input('Enter number to find out square root: '))
# print(f'Square root of {my_num} is: ', math.sqrt(my_num))

# #--------------
# # Random Number
# import math
# import random
# print('Your luck number from 1 to 100 is: ',random.randint(1,100))

#--------------
# To check function inside module
# import math
# import inspect

# functions = inspect.getmembers(math, inspect.isbuiltin)
# print(functions)

# for n, func in functions:
#     print(n)

#--------------
# import math            # pobondo
# import inspect

# print('Sin 90 is: ',math.sin(90))       # Just to find sin 90

# deg = int(input('Degree to find out cos'))
# print(f'Cos{deg} is: ',math.cos(deg))

#--------------
import math                 # pobondo
import inspect

functions = inspect.getmembers(math, inspect.isbuiltin)
for n, func in functions:
    print(n)