# Read file

import os
# file_path = r'E:\AIML\Day 8\ourfiles'
filepath = os.getcwd()
filename = input('Enter file name to read file: ')
fullpath = os.path.join(filepath, filename)

if(os.path.exists(fullpath)):
    file = open (fullpath,'r')
    content = file.read()
    print('File content as follows: ')
    print(content)
    file.close()
else:
    print(f'No such file {filename} exist')