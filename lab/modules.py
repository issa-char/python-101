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