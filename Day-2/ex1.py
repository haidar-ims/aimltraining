#Loop Range List String

# print("First Example")
# print("1 to 9 \n")
# for i in range(10):
#     print(i)

# print("Second Example")
# print("Printing numbers from 1 to 10 \n")
# for i in range(1,11):
#     print(i)

# print("Third Example")
# for i in range(10):
#     print(i+1)

# for i in range(3,10):
#     print(i)

# Loop in One Continuous Line
# for item in range(100):
#     print(item+1,end=" ")

# Loop in Continuous Line with a Tab
# for item in range(10):
#     print(item+1,end="\t")

# employees=['Sudin','Kadir','Budin']
# for e in employees:
#     print(e)

# products=['Kacang','Pisang','Bayam','Timun']
# for item in products:
#     print(item)

# for ch in 'Nexpert Academy':
#     print(ch,end="-> ")

# for ch in 'Nexpert Academy':
#     print(ch,end=" ")

# yourName=input("Enter Your Name: \t")
# print('Characters of your name as follows: \n')
# for ch in yourName:
#     print(ch)

#Request Number for Table
num=int(input('Please enter number to find out the table: \t'))
print(f'Table of Number {num} as follows \n')
for i in range(1,13):
    print(f'{num}*{i}=\t{num*i}')

#Tuple - A tuple is an immutable data type in python.
#One example of tuple using for loop

# players=('MSD','VK','KL','RS')
# for players in players:
#     print(players)

# players=('Messi','Veron','Kane','Ronaldo')
# for player in players:
#     print(player[0])

players=('Messi','Veron','Kane','Ronaldo')
for player in players:
    print(player,end=" ")