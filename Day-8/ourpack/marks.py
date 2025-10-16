class InvalidMarks (Exception):
    pass

def check_marks(marks):
    if (marks<0):
        raise InvalidMarks ('Nothing less than 0')
    elif(marks>50):
        raise InvalidMarks ('Not more than 50')
    else:
        print (f'Your marks is {marks}, Thank you for your input.')
