import math
# num = int(input("Enter any Number : "))
# if num<0:
#     print("You enter negative number")
# elif (num%2==0):
#     print("Even Number")
# else:
#     print("Odd Number")


# value1 = False
# value2 = False


# if(value1 and value2):
#     print("Both value are true")

# elif (value1 or value2):
#     print("One value is true")
# else:
#     print("Both value are false")


# practise set
# Write a program to find the greatest of four numbers entered by the user.

# 1 problem
# a1=int(input("Enter number 1 : "))
# a2=int(input("Enter number 2 : "))
# a3=int(input("Enter number 3 : "))
# a4=int(input("Enter number 4 : "))

# if(a1>a2 and a1>a3 and a1>a4):
#     print("A1 is greater")
# elif(a2>a1 and a2>a3 and a2>a4):
#     print("A2 is greater")
# elif(a3>a1 and a3>a2 and a3>a4):
#     print("A3 is greater")
# elif(a4>a1 and a4>a3 and a4>a2):
#     print("A4 is greater")
# else:
#     print("Number are same")


# 2 problem
# Write a program to find out whether a student has passed or failed if it requires a
# total of 40% and at least 33% in each subject to pass. Assume 3 subjects and
# take marks as an input from the user.

# marks1=int(input("Enter marks 1 : "))
# marks2=int(input("Enter marks 2 : "))
# marks3=int(input("Enter marks 3 : "))

# total_precentage = ((marks1+marks2+marks3)/300)*100
# print(round(total_precentage,2))

# if(total_precentage>=40 and marks1 > 33 and marks2 > 33 and marks3 > 33):
#     print(f"You are pass with {round(total_precentage,2)}")
# else:
#     print(f"You are fail because your precentage is {round(total_precentage,2)}")


# 3 problem
# A spam comment is defined as a text containing following keywords:
# “Make a lot of money”, “buy now”, “subscribe this”, “click this”. Write a program
# to detect these spams.

# p1="Make a lot of money"
# p2="buy now"
# p3="subscribe this"
# p4="click this"

# message = input("Enter you comment : ")

# if((p1 in message) or (p2 in message) or (p3 in message)):
#     print("This comment is spem")
# else:
#     print("No any spem")


# 4 problem
# Write a program to find whether a given username contains less than 10
# characters or not.

# name = input("Enter your name : ")
# if(len(name) < 10):
#     print("Name is lesser then 10 character")
# else:
#     print("Name is greater then and above 10 charater")


# 5 problem
# Write a program which finds out whether a given name is present in a list or not.

# my_list = ["Varun","Udit","Nitin","Vinayak","Vishal","Rahul","Adatya"]
# name = input("Enter your friend name : ")

# if(name in my_list):
#     print(f"{name} is abilavle in your friend list")
# else:
#     print(f"{name} is not abilavle in your friend list")


# 6 problem
# Write a program to calculate the grade of a student from his marks 

# marks = int(input("Enter marks between 1 to 100 : "))

# if(marks >=90):
#     print("Graed EX")
# elif(marks >= 80):
#     print("Gread A")
# elif(marks >= 70):
#     print("Gread B")
# elif(marks >= 60):
#     print("Gread C")
# elif(marks >= 50):
#     print("Gread D")
# else:
#     print("Fail")


# 7 problem
# Write a program to find out whether a given post is talking about “Harry” or not

# post = input("Enter post description : ")
# name = "Varun"

# if(name in post):
#     print("Name is heare ")
# else:
#     print("Name is not heare priesent")