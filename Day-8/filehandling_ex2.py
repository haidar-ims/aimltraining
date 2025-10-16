# Append

import os
# file_path = r'E:\AIML\Day 8\ourfiles'
filepath = os.getcwd()
filename = input('Enter file name to update file: ')
fullpath = os.path.join(filepath, filename)

if(os.path.exists(fullpath)):
    file = open (fullpath,'a')
    content = input('Enter text to add in file: ')
    file.write(content)
    print(f'File {filename} updated')
    file.close()
else:
    print(f'No such file {filename} exist')