from ourpack import calc
while True:
    try:
        fnum = float(input('Enter first number: '))
        snum = float(input('Enter second number: '))
        op = input('Choose operation +, -, * or /: ')
        if(op == '+'):
            print('Result:\t', calc.add(fnum,snum))
        elif(op=='-'):
            print('Result:\t', calc.sub(fnum,snum))
        elif(op=='*'):
            print('Result:\t', calc.multi(fnum,snum))
        elif(op=='/'):
            print('Result:\t', calc.div(fnum,snum))
        else:
            raise ValueError
        
    except ZeroDivisionError as ze:            # Specific Exception
        print('Division by 0 not allowed',ze)
    except ValueError as ve:                  # Specific Exception
        print('Error in values',ve)
    except Exception as e:    # General Exception * Placed last after specific Exception
        print('Error!',e)
    choice = input('Do you want to continue? If yes press Y').lower() #lower to change y to uppercase
    if(choice!='y'):
        print('Bye')
        break

