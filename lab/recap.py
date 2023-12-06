# Data Structures
# lists, dictionaries, tuples, strings, sets, numbers

# numbers (float, integers, complex)
# complex numbers are numbers with real and imaginary parts
# intergers are whole numbers
# float are numbers with decimal points
# numbers can be converted to other types
# int(), float(), complex()
a = 77  # int
b = 87.9    # float
c = 1 + 2j  # complex
d = float(77)   # convert to float
e = complex(b)  # convert to complex
f = int(b)  # convert to int
print(a, b, c, d, e, f)
# math operations (+, -, *, /, %, **, //)
# + addition, - subtraction, * multiplication, / division, % modulus, ** exponent, // floor division
# floor division is division that results into whole number adjusted to the left in the number line
# division results into float
# floor division results into integer
X = 88 // 3
z = 99 / 3
print(X, z)
# modulus results into remainder of the division
V = 88 % 3
print(V)
# exponent results into raised to power of the number 
r = 2**3
print(r)
# order of operations (PEMDAS)
g = 2 + 3 * 5 / 2 - 1
# parentheses can be used for grouping
h = (2 + 3) * 5 / 2 - 1
print(g, h)

# strings
# strings represented as str and enclosed within (single, double, triple quotes) 
# triple quotes are used for multi-line strings
# strings are immutable (cannot be changed)
# strings can be sliced using slice operator ([:])
# strings can be concatenated using + operator
# strings can be repeated using * operator
# strings can be searched using in and not in operators
# strings can be formatted using % operator
# strings can be formatted using format() method
# strings can be formatted using f-strings
# strings can be formatted using template strings
# strings can be formatted using string interpolation
# strings can be formatted using string modulo operator
fname = "Christian"
lname = 'Ino'
man = '''
read carefully through this manual, dev takes no responsibility for system break
name [OPTIONS]

-h              you are looking at it
-g ip           you ip details
'''
print(man)
print(fname[-1:3])
print(lname[1])
print(fname + lname) # concatenation
print(fname * 3) # repetition
print('C' in fname) # search
print('C' not in fname) # search

# lists
# lists are mutable (can be changed)
# lists are enclosed within square brackets [] and the elements are separated by commas
# lists can be sliced using slice operator ([:])
# lists can be concatenated using + operator
# lists can be repeated using * operator
# lists can be searched using in and not in operators
results = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(results[2:5])
print(results + results)
print(results * 3)
print(3 in results)
print(3 not in results)
# lists can be added using append() method
# lists can be added using extend() method
# lists can be added using insert() method
# lists can be removed using remove() method
# lists can be removed using pop() method
# lists can be removed using del keyword
# lists can be removed using clear() method
results.append(10)
results.extend([11, 12, 13])
results.insert(0, 0)
print(results)
results.remove(0)
results.pop(10)
del results[0]
print(results)
results.clear()
print(results)
# lists can be sorted using sort() method
# lists can be sorted using sorted() function
# lists can be reversed using reverse() method
# lists can be reversed using reversed() function
# lists can be counted using count() method
# lists can be counted using len() function
# lists can be counted using index() method
# lists can be counted using sum() function
# lists can be counted using min() function
# lists can be counted using max() function
scores = [1, 2, 3, 4, 5, 6, 7, 8, 9]
scores.sort()
print(scores)
print(sorted(scores))
scores.reverse()
print(scores)
print(list(reversed(scores)))
print(scores.count(1))
print(len(scores))
print(scores.index(1))
print(sum(scores))
print(min(scores))
print(max(scores))
# lists can be copied using copy() method
# lists can be copied using list() function
# lists can be copied using slice operator ([:])
# lists can be copied using deepcopy() method
items = ['books', 'pens', 'phone', 'charger', 'laptop', 'mouse', 'keyboard', 'earphones']
print(items)
n_items = items.copy()
print(n_items)
print(items[2:5])
print(items[:])
import copy
n_items = copy.deepcopy(items)
print(n_items)

# tuples
# tuples are immutable (cannot be changed)
# tuples are enclosed within parentheses () and the elements are separated by commas
# tuples can be sliced using slice operator ([:])
user = ('Christian', 'Ino', 23)
print(user[0])
# tuples can be concatenated using + operator
# tuples can be repeated using * operator
# tuples can be searched using in and not in operators
# tuples can be added using + operator
# tuples can be added using += operator
# tuples can be added using tuple() function
# tuples can be added using count() method
# tuples can be added using index() method
hobbies = ('reading', 'coding', 'gaming')
print(user + hobbies)
print(user * 3)
print('Christian' in user)
print('Christian' not in user)

# Dictionary
# dictionaries are mutable (can be changed)
# dictionaries are enclosed within curly braces {} and the elements are separated by commas
# dictionaries are key-value pairs (keys are unique) and the values can be of any type
course = {"name": "Python", "duration": "3 months", "price": 1000}
print(course["name"])
# dictionaries can be concatenated using + operator
# dictionaries can be repeated using * operator
# dictionaries can be searched using in and not in operators
# dictionaries can be added using update() method
# dictionaries can be added using copy() method
# dictionaries can be added using dict() function
# dictionaries can be added using clear() method
# dictionaries can be removed using pop() method
# dictionaries can be removed using popitem() method
# dictionaries can be removed using del keyword
s_course = {"name": "JavaScript", "duration": "3 months", "price": 1000}
# print(course + s_course)
#print(course * 3)
print("name" in course)
print("name" not in course)
course.update(s_course)
print(course)

# sets

# control statements

# Modules
# modules are files containing python code
# modules can be imported using import keyword
import sys
# modules can be imported using from keyword
from sys import platform
# modules can be imported using as keyword
import sys as system

