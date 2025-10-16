# # Today's Date

# import datetime
# print('The date for today is: ',datetime.date.today())

# #--------------
# import datetime
# import inspect

# dtclasses = inspect.getmembers (datetime, inspect.isclass)
# print('All Classes inside datetime module')

# for n, func in dtclasses:
#     print(n)

# print('All functions inside datetime.date class')

# functions = inspect.getmembers(datetime.date, inspect.isbuiltin)
# for n, func in functions:
#     print(n)

# print('Today is (Date):', datetime.date.today())

#--------------
# import os
# import inspect
# functions = inspect.getmembers(os, inspect.isbuiltin)
# for n, func in functions:
#     print(n)

#--------------
import os
listDirs = os.listdir()
for dir in listDirs:
    print(dir)
