# os module; interact with system OS
import os

for i in dir(os):
    print(i, end="->")

print("\n")
print(os.uname()) # system info
print(os.name)  # posix for unix, nt for windows and java for code in jython
try:
    print(os.mkdir("dir1")) # create a dir
except:
    print("directory exists")

try:
    os.makedirs("mydir2/mydir3/mydir4/mydir5") #recursive dir creation
except:
    print("dir exits")

print(os.listdir()) # print cotents of dir
print(os.getcwd()) # return info about the current working dir
#os.removedirs("mydir2")
os.rmdir("dir1")
print(os.system("myd"))

## ASSIGNMENT





# datetime and time module; provides classes for working with date and time
# applications: event loggging, data validation, storing important info, tracking changes in the database
import datetime

for i in dir(datetime):
    print(i, end="-->")

print("\n")
today = datetime.date.today()
print(today)














# ASSIGNMENT












# calendar module