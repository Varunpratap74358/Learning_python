
# single inheritance
# class Animal:
#     def speek(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# d = Dog()
# d.speek()
# d.bark()


#  multilevel inheritance
# class Animal:
#     def speek(self):
#         print("Animal speaks")

# class Dog(Animal):
#     def bark(self):
#         print("Dog barks")

# class Puppy(Dog):
#     def cute(self):
#         print("Puppy i cute")

# d = Puppy()
# d.speek()
# d.bark()
# d.cute()


# multipale inheritance
# class Mother:
#     def cook(self):
#         print("Mother cooks")
# class Father:
#     def drive(self):
#         print("Father drive")
# class Child(Mother,Father):
#     def play(self):
#         print("Child play")

# c = Child()
# c.cook()
# c.drive()
# c.play()




# Hierachical Inheritance
# class Mother:
#     def cook(self):
#         print("Mother cooks")
# class Father(Mother):
#     def drive(self):
#         print("Father drive")
# class Child(Father):
#     def play(self):
#         print("Child play")

# f = Father()
# c = Child()
# f.cook()
# c.drive()
# c.play()




'''
    inheritance (Done)
    polymorphism
    abstraction
    encaptulation

'''


# # super keyword
# class Mother:
#     def __init__(self):
#         print("This is constructor of Mother")
#     def cook(self):
#         print("Mother cooks")
# class Father:
#     def __init__(self):
#         super().__init__()
#         print("This is constructor of Father")
#     def drive(self):
#         print("Father drive")
# class Child(Father,Mother):
#     def __init__(self):
#         super().__init__()
#         print("This is constructor of Child")
#     def play(self):
#         print("Child play")

# c = Child()
# c.cook()
# c.drive()
# c.play()




# class Emp:
#     a = 1
#     @classmethod #this is use to show the class attribute not show the instance attribute
#     def show(self):
#         print(f"The class attribute of a is {self.a}")

# e = Emp()
# e.a = 10
# e.show()





# preactice set
# 1problem
# class TwoDVector:
#     def __init__(self,i,j):
#         self.i = i
#         self.j = j
    
#     def show(self):
#         print(f"The vactor is {self.i}i + {self.j}j")
    
# class ThreeDVector(TwoDVector):
#     def __init__(self,i,j,k):
#         super().__init__(i,j)
#         self.k = k
#     def show(self):
#         print(f"The vactor is {self.i}i + {self.j}j + {self.k}k")
    
# a = TwoDVector(1,2)
# a.show()
# b = ThreeDVector(5,2,3)
# b.show()



# 2 problem

# class Animal:
#     pass

# class Pets(Animal):
#     pass

# class Dog(Pets):
#     @staticmethod
#     def barks(n):
#         print("Baw Baw")
    

# d = Dog()
# d.barks()



# 3 problem

# class Employee:
#     salary = 234
#     inc = 20
#     # @property
#     def salaryAfterInc(self):
#         return (self.salary + self.salary*(self.inc/100))
    
# e = Employee()
# print(e.salaryAfterInc())


# 4 problem
# class Complex:
#     def __init__(self,r,i):
#         self.r = r
#         self.i = i
#     def __add__(self,c2):
#         return Complex(self.r + c2.r , self.i + c2.i)

#     def __mul__(self,c2):
#         real_part = self.r*c2.r - self.i*c2.i
#         imag_part = self.r*c2.i + self.i*c2.r
#         return Complex(real_part,imag_part)

#     def __str__(self):
#         return f"{self.r} + {self.i}i"


# c1 = Complex(1,2)
# c2 = Complex(3,4)
# print(c1 + c2)
# print(c1 * c2)


