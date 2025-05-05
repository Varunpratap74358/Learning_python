
# def greet(name):
#     return f"Hello {name}"


# l = ["Varun","Nitin","Udit","Vinayak"]

# for i in l:
#     print(greet(i))


# default parameter
# def goodDay(name="Varun"):
#     print(name)

# goodDay()
# goodDay("Singh")


# recursion

# def factorial(n):
#     if(n==1 or n==0):
#         return 1
#     else:
#         return n*factorial(n-1)
    
# print(factorial(5))
# print(factorial(6))
# print(factorial(7))

# def fibonacci(n):
#     if(n<=0):
#         return 0
#     elif n==1:
#         return 1
#     else:
#         return fibonacci(n-1) + fibonacci(n-2)

# num = int(input("Enter number : "))
# for i in range(num):
#     print(fibonacci(i),end=" ")


# prectice set

# 1. Write a program using functions to find greatest of three numbers.

# def gretestNumber(n1,n2,n3):
#     if(n1>n2 and n1>n3):
#         print(f"{n1} is greater")
#     elif(n2>n3):
#         print(f"{n2} greater")
#     else:
#         print(f'{n3} is greater')

# gretestNumber(5,4,8)
# gretestNumber(9,5,4)