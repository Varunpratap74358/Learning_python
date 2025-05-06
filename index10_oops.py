
# class employee:
#     name = "Varun"
#     language = "JAVASCRIPT"
#     salary = 500000

# varun = employee()
# print(varun.name)
# print(varun.language)
# print(varun.salary)





# class student:
#     def __init__(self,name,age): # this is constuctor
#         self.name = name
#         self.age = age
    
#     def showInfo(self):
#         print(f"Name of student is {self.name} and age is {self.age}")

#     def sayGood(self):  # self is required for method
#         print("Hello good morning")

#     @staticmethod # no need to write self
#     def sayHello():
#         print("Hello varun")

# # s1 = student("Varun",20)
# # s1.showInfo()
# s2 = student("Nitin",21)
# s2.showInfo()
# s2.sayGood()
# s2.sayHello()




# practice set

# 1 Create a class “Programmer” for storing information of few programmers working at Microsoft.

# class Programmer:
#     def __init__(self,name,age,language):
#         self.name = name
#         self.age = age
#         self.language = language
    
#     def shoInfo(self):
#         print(f"Name of programer is : {self.name} and age is : {self.age} and he is working on {self.language}")


# obj1 = Programmer("Varun",20,"JavaScript")
# obj1.shoInfo()


# 2 Write a class “Calculator” capable of finding square, cube and square root of a number

# class calculator:
#     def __init__(self,n):
#         self.n = n
#     def squire(self):
#         print("Squire is : ",self.n*self.n)

#     def cube(self):
#         print("Cube is : ",self.n*self.n*self.n)
    
#     def squireRoot(self):
#         print("The squire root is : ",self.n**(1/2))


# o1 = calculator(25)
# o1.squire()
# o1.cube()
# o1.squireRoot()


# 3 problem

# class Demo:
#     a = 4
# o = Demo()
# print(o.a)
# o.a = 2
# print(o.a)

# 4 problem
# from random import randint
# class Train:
#     def __init__(self,trainNo):
#         self.trainNo = trainNo
#     def book(self,fro,to):
#         print(f"Ticket is Booked train no : {self.trainNo} from {fro} to {to}")
    
#     def getStatus(self):
#         print(f"{self.trainNo} is running successfully... ")
    
#     def getFare(self,fro,to):
#         print(f"Ticket fare in  train no : {self.trainNo} from {fro} to {to} is {randint(255,555)}")
    
# t1 = Train(25456)
# t1.book("SPN","HAD")
# t1.getStatus()
# t1.getFare("SPN","HAD")