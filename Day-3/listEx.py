#print("List Example One")

# my_list=[10,20,30, "Python",None,True,12.45,'Raju']
# print('Number of items in list are:',len(my_list))
# for item in my_list:
#     print(item)

# print("Second Example of List")
# emps=["Samad","Kadir","Ahmad","Zaid"]
# print("Number of Employees",len(emps))
# print('All Employees')
# # for emp in emps:             #List Result
# #     print(emp)

# for emp in emps:               #One Line Result
#     print(emp,end=" ")



# #Sort Example
# #listName.sort()
# emps.sort()
# print("\nList After Sorting")
# for e in emps:
#     print(e, end=" ")

# #Reverse Example
# #listName.reverse()
# emps.reverse()
# print('\n Employee in Descending Order')
# for e in emps:
#         print(e, end=" ")

#append,remove,pop and insert method

# emps=["Samad","Kadir","Ahmad","Zaid"]
# print("Number of Employees",len(emps))
# for emp in emps:               #One Line Result
#     print(emp,end=" ")

    #append: adds at the end of the list
# newEmp=input("\nEnter employee name to add in list: ")
# emps.append(newEmp)
# print('\nAfter addiing New Employee: Number of employees are:',len(emps))
# for emp in emps:
#     print(emp,end=" ")

#insert(index,item): This will add item at given index
# newEmp=input("\nEnter employee name to add in list: ")
# pos=int(input("\nEnter employee name to add in list:\t"))                      #prob
# emps.insert(pos,newEmp)
# print('\nAfter addiing New Employee: Number of employees are:',len(emps))
# for emp in emps:
#     print(emp,end=" ")

# emps=["Samad","Kadir","Ahmad","Zaid"]
# print("Number of Employees",len(emps))
# for emp in emps:               #One Line Result                     #prob
#     print(emp,end=" ")
# #listName.remove: Will remove item from the list.
# delEmp=input('employee to remove in list:\t')
# if delEmp in emps:
#     emps.remove(delEmp)
#     print(f"Number of employeeafter deleting {delEmp} in list are:",len(emps))
#     for emp in emps:
#     print(emp,end=" ")
# else:
#     print(f'No such item {delEmp} in employee list')

#pop() example
#listName.pop(index): Will delete element at given index and return its value.
# emps=["Samad","Kadir","Ahmad","Zaid"]
# print("Number of Employees",len(emps))
# for emp in emps:               #One Line Result
#     print(emp,end=" ")
# del_index=int(input('eenter index to pop item:\t'))
# print('pop result: ',emps.pop(del_index))
# print("number of employee after pop() are:",len(emps))
# for emp in emps:
#     print(emp,end=" ")

#find out first and last element
emps=["Samad","Kadir","Ahmad","Zaid"]
print("Number of Employees",len(emps))
for emp in emps:               #One Line Result
    print(emp,end=" ")
print('\n First Element of employees list it: ',emps[0])
print('\n last Element of employees list it: ',emps[-1])