
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

# 2 Write a python program using function to convert Celsius to Fahrenheit.

# def celsius_to_fahrenheit(celsius):
#     result = (celsius*9/5)+32
#     return result

# num = float(input("Enter temperature in celsius : "))
# result = celsius_to_fahrenheit(num)

# print(f"{num}°C is equal to {result}°F")




# 3 How do you prevent a python print() function to print a new line at the end.
# print("A")
# print("B")
# print("C",end=" ")
# print("D",end="")


# 4 Write a recursive function to calculate the sum of first n natural numbers.
# def naturalSum(num):
#     if(num==1 or num<=0):
#         return 1
#     return num+naturalSum(num-1)

# print(naturalSum(10))
# print(naturalSum(11))
# print(naturalSum(12))


# 5 pattern
# def pattern(n):
#     if(n==0):
#         return
#     print(" * "*n)
#     pattern(n-1)

# pattern(3)


# 6 inch to cms
# def inch_to_cms(inch):
#     return inch*2.54
# n = int(input("Enter inch number  : "))
# print(inch_to_cms(n))



# 7 Write a python function to remove a given word from a list ad strip it at the same time

# def rem(l,word):
#     for item in l:
#         l.remove(word)
#         return l

# l = ["Varun","Nitin","Singh","Vinayak"]
# res = rem(l,"Singh")
# print(res)


# 8 Write a python function to print multiplication table of a given number.
# def table(n):
#     for i in range(1,11):
#         print(n*i)
#     return
# n = int(input("Enter number : "))
# table(n)