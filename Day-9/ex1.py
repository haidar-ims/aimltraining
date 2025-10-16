#Write a function to check a number is odd or even
def check_odd_even(number):
    if (number%2==0):
        print (f'{number} is Even')
    else:
        print(f'{number} is Odd')

given_number=int(input('Enter Number:\t'))
check_odd_even(given_number)