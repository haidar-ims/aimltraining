class InvalidAge (Exception):
    pass

def check_age(age):
    if (age<=0):
        raise InvalidAge ('Wait till you are born and 18 and above')
    elif(age<18):
        raise InvalidAge ('Age should be above 18')
    elif(age>=80):
        raise InvalidAge ("Sorry, it's time to retire and enjoy life ")
    else:
        print (f'Age {age} is accepted and valid age for employment')

try:
    userage = int(input('Enter your age: '))
    check_age (userage)
except InvalidAge as e:
    print('Invalid Age! ',e)
except Exception as ex:
    print('Error!',ex)