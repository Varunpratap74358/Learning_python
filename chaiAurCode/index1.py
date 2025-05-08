
# problem 1 : find how many postive and how many negative number in given list
# n = 0
# p = 0
# l1 = [1,-2,3,-4,5,6,-7,-8,9,10]
# for i in l1:
#     if i<0:
#         n+=1
#     else:
#         p += 1

# print(f"Number os negative number in l1 is  : {n} and pisitive is : {p}")



# problem 2 : sum of even number
# n = 10
# sum_even = 0
# for i in range(1,n+1):
#     if i%2==0:
#         sum_even+=i

# print(f"Sum of even number is : {sum_even}")


# problem 3 : print the multiplication table for a given number up to 10. but skip the 5 iteration
# num = int(input("Enter any number : "))
# for i in range(1,11):
#     if(i==5):
#         continue
#     else:
#         print(num*i)



# problem 3 : reverse a string
# s = "Varun Singh"
# rev = s[::-1]
# print(rev)
# rev1 = "".join(reversed(s))




# problem 4 : find the first repeted character
# def repted_char(s):
#     for i in s:
#         if s.count(i)==1:
#             return i
#     return None
# text = "aabbcdesef"
# print(repted_char(text))



# problem 4 : validate input
# while(True):
#     num = int(input("Enter value b/t 1 to 10 : "))
#     if 1 <= num <= 10:
#         print("Thanks")
#         break
#     else:
#         print("Invalid number - Enter valid number")



# problem 5 : list uniqueness chacker
# items = ["apple","banana","orange","apple","mango"]
# unique_item = set()

# for item in items:
#     if item in unique_item:
#         print("Duplicate",item)
#         break
#     unique_item.add(item)



# problem 6 : Exponetial Backoff
import time

wait_time = 1
max_retries = 3
attempts = 0

while attempts < max_retries:
    print(f"Attempt : {attempts+1} - wait time {wait_time} ")
    time.sleep(wait_time)
    wait_time *= 2
    attempts+=1
print("Thanks")