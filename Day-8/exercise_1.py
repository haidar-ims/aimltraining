#Take user marks from user with in 0 to 50
#if user enter outside [0-50] raise Error InvlidMarks using Custom Exception
#Give chance to the user till, he/she entered valid marks

from ourpack import marks

while True:
    try:
        usermarks = int(input('Enter your marks [0-50]: '))
        marks.check_marks (usermarks)
    except marks.InvalidMarks as e:
        print('Invalid Marks!',e)
    except Exception as ex:
        print('Error!',ex)
    else:
        print("It's in our record now.")
        break
    choice = input('Would you like to re-enter marks? if yes press Y or exit with any key: ').lower()
    if(choice!='y'):     # != means not equal to
        print('Bye')
        break