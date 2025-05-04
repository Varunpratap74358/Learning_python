
name="varun singh"
print(name)

shortName = name[1:5]
# print(shortName)

# print(name[:]) # return full name
# print(name[1:4:2]) # return full name


# print(name.endswith("run")) #FALSE
# print(name.capitalize())
# print(name.upper())
# print(name.title())
# print(name.find("singh"))

string = "Varun is a good boy and he is loyal for his GF "
print(string.replace("good",'bad')) #replace good to bad
print(string.strip())#Removes whitespace from the beginning and end.

print(string.split())

words = string.split()
result = ' '.join(words)
print(result)

