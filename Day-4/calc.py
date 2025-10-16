def add(num1,num2):
    return (num1+num2)

def multi(num1,num2):
    return (num1*num2)

def avg(num1,num2):
    return (num1+num2)/2

def sub(num1,num2):
    return (num1-num2)

def div(num1,num2):
    return (num1/num2)
print("Welcome to Calculator")
while True:
    print('Select operation \n1.Add \n2.Sub \n3.Multi \n4.Division \n5.Average \n6.Exit ')
    op=int(input('Enetr your operation choice(1-6):\t'))
    if(op==6):
        print('Goodbye')
        break
    if(op>=6) or (op<=0):
        print('Wroong operation choice, Only 1 to 6 are allowed')
    else:
        fnum=float(input('Enter First Number:\t'))
        snum=float(input('Enter Second Number:\t'))
        if(op==1):
                print(f'Result after adding{fnum},{snum}:\t',add(fnum,snum))
        elif(op==2):
                print(f'Result after subtracting {fnum} from {snum}:\t',sub(fnum,snum))
        elif(op==3):
                print(f'Result after multiplying{fnum},{snum}:\t',multi(fnum,snum))
        elif(op==4):
                print(f'Result after dividing{fnum} by {snum}:\t',div(fnum,snum))
        elif(op==5):
                print(f'Average of {fnum} and {snum}:\t',avg(fnum,snum))