# print("We are going to discuss Tuple here")
# subjects=('python','java','power bi','dotnet','sql')
# print('\n All subjects are:\n')
# print('Number of subjects are: ',len(subjects))
# for sub in subjects:
#     print(sub,end="\t")

# numbers=(1,2,3,4,10,2,3,2,3,5,50)
# print('Total Number in Tuple: ',len(numbers))                #Check
# for num in numbers:
#     print(num,end="\t")

#tupleName.index(item) will return in the index of first occurence of item in tupleName.
# search_num=int(input('Enter number to find out index: '))
# if search_num in numbers:
#     print(f'Index of {search_num} is: \t',numbers.index(search_num))
# else:
#     print(f'No Such Number {search_num} in our tuple')

#tupleName.count (item): tupleName count (item) will return number of times item occurs in tupleName.
# numbers=(1,2,3,4,10,2,3,2,3,5,50)
# print('Total Number in Tuple: ',len(numbers))
# for num in numbers:
#     print(num,end="\t")
# search_num=int(input('Enter number to find out frequency:\t'))
# if search_num in numbers:
#     print(f'Number: {search_num} occurs: {numbers.count(search_num)} times')
# else:
#     print(f'No Such Number {search_num} in our tuple')

#Write a program to sum a list with 4 numbers.
numbers=[3,5,2]
total=sum(numbers)
print('The sum is:',total )