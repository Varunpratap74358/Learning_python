from color50 import rgb, constants
import pyttsx3
import os

my_color = rgb(255,0,0)
print(my_color + "Hello, World!" + constants.RESET)


directory_path = '/zzz/public'
contents = os.listdir(directory_path)
# for item in contents:
#     print(item)

print(contents)


engine = pyttsx3.init()
engine.say("Hay, I am Varun Pratap Singh, and I am a mern stack developer, and i am currently pursuing BCA at Future college")
engine.runAndWait()