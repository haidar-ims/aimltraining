# import os
# # file_path = r'E:\AIML\Day 8\ourfiles\sample.txt'
# file_path = 'E:\\AIML\\Day 8\\ourfiles\\sample.txt'

# file = open (file_path,'w')
# content = input('Enter text to write in file: ')
# file.write(content)
# file.close()

# #------------------------
# # Create File and Path then Write

# import os
# # file_path = r'E:\AIML\Day 8\ourfiles'
# filepath = 'E:\\AIML\\Day 8\\ourfiles'
# filename = input('Enter file name to create file: ')
# fullpath = os.path.join(filepath, filename)
# file = open (fullpath,'w')
# content = input('Enter text to write in file: ')
# file.write(content)
# print(f'File {filename} create at {fullpath} and content saved in file')
# file.close()

#------------------------
# Get Current File Path then Write

import os
# file_path = r'E:\AIML\Day 8\ourfiles'
filepath = os.getcwd()
filename = input('Enter file name to create file: ')
fullpath = os.path.join(filepath, filename)
file = open (fullpath,'w')
content = input('Enter text to write in file: ')
file.write(content)
print(f'File {filename} create at {fullpath} and content saved in file')
file.close()



