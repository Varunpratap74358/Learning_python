# Creating a dictionary
my_dict = {
    "name": "Rahul",
    "age": 25,
    "course": "Python"
}

# print(my_dict["name"])

# for key, value in my_dict.items():
#     print(key," : ",value)


# methods
# print(my_dict.items())
# print(my_dict.keys())
# print(my_dict.values())
# my_dict.update({"age":20}) #this is update the dist
# my_dict.update({"phone":8601686595}) #this is add the property if this is not exist in the dist
# print(my_dict)# this is print all the dist data
# print(my_dict.get('name'))
# print(my_dict.get('city'))

# item = my_dict.pop("name")
# print(item)
# my_dict.setdefault("city","SPN")
# print(my_dict)





#problem in sets
es = set() #this is use for create the empty set
# print(type(es))

s={1,5,7,8,9,6,4,8,1,5} #values are not repeted
# s.add(10) #add 10 in the set
# s.remove(5) #remove 5 in the set
# s.update([20,30]) #add multiple element in the set
# rem = s.pop()
# print(rem)
# print(s)

set1={1,5,7,8,9,6}
set2={2,12,11,15}
# remove = set1.pop()
# print(remove)

# print(set1)

# s1={1,45,6}
# s2={7,8,1,78}
# print(s1.union(s2))
# print(s1.intersection(s2))



# prectise set
# 1 problem
# words={
#     "aam":"mango",
#     "kela":"banana",
#     "angur":"grapes"
# }
# word = input("Enter th word you want meaning : ")
# print(words[word])

# 2 problem
# inpu1 = int(input("Enter number : "))
# inpu2 = int(input("Enter number : "))
# inpu3 = int(input("Enter number : "))
# inpu4 = int(input("Enter number : "))
# inpu5 = int(input("Enter number : "))
# inpu6 = int(input("Enter number : "))
# inpu7 = int(input("Enter number : "))
# inpu8 = int(input("Enter number : "))
# mySet = {inpu1,inpu2,inpu3,inpu4,inpu5,inpu6,inpu7,inpu8}
# print(mySet)

# 3 problem
# s = set()
# s.add(18)
# s.add("18")
# print(s)

# 4 problem
# s=set()
# s.add(20)
# s.add(20.0) # 20 and 20.0 are same
# s.add("20")
# print(s)
# print(len(s))


# 5 problem
# s={}
# print(type(s))


# 6 problem
# myDir = {}
# name = input("Enter friend name : ")
# lang = input("Enter language name : ")
# myDir.update({name:lang})
# name = input("Enter friend name : ")
# lang = input("Enter language name : ")
# myDir.update({name:lang})
# name = input("Enter friend name : ")
# lang = input("Enter language name : ")
# myDir.update({name:lang})
# name = input("Enter friend name : ")
# lang = input("Enter language name : ")
# myDir.update({name:lang})

# print(myDir)


# last error
# s = {8, 7, 12, "Harry", (1, 2)}
# print(s)
