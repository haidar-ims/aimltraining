# Assignment operators: =, +=, -=
# price=float(input("Enter Product Price "))
# discount=price*0.10
# disPrice=price-discount
# print(f"Price: {price} \n Discount: {discount} \nDiscounted Price:{disPrice}")

# salary=50000.50
# bonus=5000.60
# print(f"Salary {salary} and Bonus {bonus}")
# salary+=bonus           #salary=salary+bonus
# print("Salary with Bonus",salary)

# salary=50000.50
# tds=salary*0.10
# print(f"Salary {salary} and TDS {tds}")
# salary-=tds           #salary=salary-tds
# print("Salary after tax",salary)

# Comparison Operators: ==, 

# if(condition)
# #code
# else
# #code

# age=int(input("Enter your age "))
# if(age>=18):
#     print("You are eligible to cast your vote")
# else:
#     print("Sorry!!! You are not eligible")
# print("End of Program")

# marks=int(input("Enter marks percentage without '%' sign"))
# if(marks<30):
#     print("Fail in exam")
# else:
#     print("Clear in Exam")

#accessCode="wes12"
# accessCode=input("Enter Access Code")
# if(accessCode!="wes12"):
#     print("Invalid Access Code ")
# else:
#     print("Welcome to Your Course")

# == means equal
# accessCode=input("Enter Access Code: \t")
# if(accessCode=="wes12"):
#     print("Welcome to Your Course")
# else:
#     print("Invalid Access Code")

#Logical operators: and, or, not.
# physicMarks=int(input("Enter marks obtaines in Physics: "))
# cheMarks=int(input("Enter marks obtain in chemistry: "))
# mathMarks=int(input("Enter marks obtain in Mathematics: "))

# if((mathMarks>=50) and (physicMarks>=55) and (cheMarks>=60)):
#     print("You are eligible to sit in pre exam of MBBS")
# else:
#     print("You have not met the required marks")

# idProof=input("Enter ID proof you have ")
# if((idProof=="passport")or(idProof=="dl")or(idProof=="voter id")):
#     print(f"Valid Id {idProof} we accept here")
# else:
#     print("Only passport, dl and voter ID are accepted as Identity Proof")
#     print(f"{idProof}:is not valid ID here")

# mathMarks=int(input("Enter marks obtained in Mathematics: "))
# gapYear=int(input("Enter year gap if any otherwise 0 "))
# if((mathMarks<=55) and (gapYear != 0)):
#     print('Not Eligible for BTech')
# else:
#     print("Eligible for Btech")

name=input("Enter User Name")
if(not name):
    print("Error!!!")
else:
    print("Welcome",name)