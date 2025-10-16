# Sets in Python
# A Set is a collection of unique items.
# It does NOT allow duplicates and is unordered.
set_one={'laptop','earphone','laptop','mobile','headphone','ipad'}
print('Number of items in set_one are: ',len(set_one))
for item in set_one:
    print(item,end=" ")

#clear(): Clearing All Items from a Set *Note: Combine top to run Clear
set_one.clear()
print('\nAfter Clear Number of items in set_one are: ',len(set_one))      #check
for item in set_one:
    print(item,end=" ")


# set_one={'laptop','earphone','laptop','mobile','headphone','ipad'}
# print('Number of items in set_one are: ',len(set_one))
# for item in set_one:
#     print(item,end=" ")
#set.remove(item): updates the set and removes item for set.
# set_one.remove('earphone')
# print('\n After removing item from one set:',len(set_one))
# for item in set_one:
#     print(item,end=" ")


# Union,intersection,difference
# Union: returns a new set with all items from both sets using .union()
# set_one={100,200,300,500,700,900,150}                  
# set_two={100,400,700,1000,1300}
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# unionset=set_one.union(set_two)
# print(f'Union of set_one and set_two contains: {len(unionset)} following items')
# print(unionset)

#intersection
# set_one={100,200,300,500,700,900,150}                  
# set_two={100,400,700,1000,1300}
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# newset=set_one.intersection(set_two)
# print(f'intersection of set_one and set_two contains: {len(newset)} following items')
# print(newset)

#difference
#s1.difference(s2): Return set which contains only item those are in s1 but not in s2..
# set_one={100,200,300,500,700,900,150}                  
# set_two={100,400,700,1000,1300}
# print(f'set_one contains: {len(set_one)} items')
# print(set_one)
# print(f'set_two contains: {len(set_two)} items')
# print(set_two)
# newset=set_one.difference(set_two)
# print(f'difference of set_one and set_two contains: {len(newset)} following items')
# print(newset)
