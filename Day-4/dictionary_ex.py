# employee={"id":1,
#          "name":"Sudin",
#          "Salary":55000.50
#          }

# print("Employees Details as follows:")
# for key, value in employee.items():
#     print(key, "->", value)

# employee["city"]="Muscat"                       #adding key in dictionary
# print('\nDictionary after adding city\n')

# for key, value in employee.items():
#     print(key, "->", value)

# del employee["salary"]
# print("\n Employee details after deleting salary \n")
# for key, value in employee.items():
#     print(key, "->", value)
#==============================
employee={"id":1,
         "name":"Sudin",
         "Salary":55000.50
         }
#-----------------------------
print('All keys from Employee')
for v in employee.keys():
    print(v,end="\t")
#------------------------------
print('\nAll values from Employee')
for v in employee.values():
    print(v,end="\t")
#-------------------------------
print('\n Key : Value')
for v in employee.items():
    print(v,end="\t")
#--------------------------------
print('\nDictionary as follows')
print(employee)
#-------------------------------
del employee["salary"]
print("\n Employee details after deleting salary \n")     #*********
for key, value in employee.items():
    print(key, "->", value)