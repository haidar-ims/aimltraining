# print('Write a function to find out the cube of given number')
#5 : 5*5*5 (e.g. cube of 5 is 5*5*5 means 125)
#5 minutes to do this task

# def cube(num):
#     return (num*num*num)

# #Cont..Correction
# given_num=int(input('Enter Number to find out cube of number:\t'))
# print(f'Number is: {given_num} cube is',cube(given_num))

#Write a function to calculate bonus of give salary
#function take salary as input and return bonus 10% of salary

def bonus(salary):
    return salary*0.10

salary=int(input('Enter Salary Amount for bonus amount:\t'))        #*float for decimal
# bonus_amount = bonus(given_salary)                       #<<<----attention
# print(f'Your bonus is: {bonus_amount} ')

print(f'Your bonus is: ',bonus(salary))                     #By guru





