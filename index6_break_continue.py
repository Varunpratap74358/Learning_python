
# break
# for i in range(1,10):
#     print(i)
#     if(i==5):
#         break


# # continue
# for i in range(1,10):
#     if(i==5):
#         continue
#     print(i)



# pass
# for i in range (1,10):
#     pass

# i=0
# while i<=5:
#     print(i)
#     i+=1




#prectise set
#1:  Write a program to print multiplication table of a given number using for loop.

# num = int(input("Enter any number : "))
# for i in range(1,11):
#     print(f"{num}*{i} = {i*num}")


# 2: Write a program to greet all the person names stored in a list ‘l’ and which starts
# with S.

# l = ["Harry", "Soham", "Sachin", "Rahul"]

# for name in l:
#     if(name.startswith("S")):
#         print(f"Hello {name}")


# 3: Attempt problem 1 using while loop.
# num = int(input("Enter any number : "))
# i=1
# while i<=10:
#     print(f"{num}*{i}={num*i}")
#     i=i+1



# 4 :Write a program to find whether a given number is prime or not.
# c=0
# n = int(input("Enter number : "))
# for i in range(1,n+1):
#     if(n%i==0):
#         c=c+1
    
# if(c==2):
#     print("Number is prime")
# else:
#     print("Not")



# 5. Write a program to find the sum of first n natural numbers using while loop.

# n = int(input("Enter number : "))
# i=0
# numSum = 0
# while i<=n:
#     numSum +=i
#     i+=1

# print(numSum)


# 6. Write a program to calculate the factorial of a given number using for loop.

# n = int(input("Enter number : "))
# i=1
# numSum = 1
# while i<=n:
#     numSum *=i
#     i+=1

# print(numSum)


# 7 problem
n = int(input("Enter number : "))
for i in range(1,n+1):
    print(" "* (n-i),end="")
    print("*"* (2*i-1),end="")
    print("")