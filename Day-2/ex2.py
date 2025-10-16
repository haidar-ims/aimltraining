# While Loop

# ourNum=1
# print('Printing Numbers from 1 to 100')
# while(ourNum<=100):
#     print(ourNum,end=" ")
#     ourNum+=1

#Break Example
# ourNum=1
# print('Printing Numbers 1 to 100 before we get the numbers divisible by 11')
# while(ourNum<=100):
#     if(ourNum%11==0):
#         break
#     print(ourNum,end=" ")
#     ourNum+=1

# #Continue and Break Example
# ourNum=1
# while(ourNum<=100):
#     if (ourNum%11==0):
#         ourNum+=1
#         continue
#     print(ourNum,end=" ")
#     ourNum+=1

#Continue and Break Example Odd Number
# ourNum=1
# while(ourNum<=100):
#     if(ourNum%2==0):
#         ourNum+=1
#         continue
#     print(ourNum,end=" ")
#     ourNum+=1

# for i in range(1,100):
#     if(i%5==0):
#         continue
#     print(i,end="\t")

# #While Loop
# correctPwd='sam1256'
# while True:
#     pwd=input('Enter Password to Start the Game: ')
#     if(correctPwd==pwd):
#         print('Welcome! Access Granted')
#         break
#     else:
#         print('Wrong Password @_@, Try Again ^_^')
# print('*** Game Started!!!***')

#While Loop 3 Chances
correctPwd='sam1256'
counter=1
while counter <= 3:
    pwd=input('Enter Password to Start the Game: ')
    if(correctPwd==pwd):
        print('Welcome! Access Granted')
        print('*** Game Started!!!***')
        break
    else:
        print('Wrong Password @_@')
        counter+=1
        if(counter>3):
            print('You have reached the limit password attempt')
            print('Blocked for 24 hours')

#While Loop 3 Chances (Method 2)
correctPwd = 'sam@1256'
counter = 0

while True:
    pwd = input('Enter Password to Start the Game:\t')

    if correctPwd == pwd:
        print('Permission Granted!!!')
        print('*** Game Started!!!! ****')
        break
    else:
        print('Wrong Password!!!')
        counter += 1

        if counter >= 3:
            print('Blocked for further Attempts')
            break
