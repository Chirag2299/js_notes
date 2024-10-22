 Chapter 1 and 2
# input for string 
name = input("Name please: ")
name2 = input("Second Name please: ")
sum = name + " " + name2  # Concatenating both names with a space
print(sum[2:])


print ("this is the first line\n\n\nthis is the second line")
print()

# input for integer
num1 = int(input("First number please: "))
num2 = int(input("Second number please: "))
result = num1 % num2  # Performing modulo operation
print(result)

indexing
str = "Api integration"
print(str[4:])
print(str.capitalize())

INDEXING--2
        str= "testing\nABC"
        print(len(str),str,str[0] is "t")

SLICING 
        print (str, str[2:9])
        print (str[0:len(str)])

String Functions 
str = "I am a coder."     ############
            str.endswith("er.") #returns true if string ends with substr 
            str.capitalize() #capitalizes 1st char 
            str.replace(old, new) #replaces all occurrences of old 
print(str.find("a") ) #returns 1st index of 1st occurrer / find("o")
print ( str.count("a") )#counts the occurrence of substr
            
###### Conditional Statements 
if-elif-else (SYNTAX)
                  
age = 33
if age >= 2200:
    print("age age aheyee")
elif age == 33:  # Use '==' for comparison
    print("munna bus")
else:
    print("mmmhmmm")
    
Chapter 3&4

Tuples

Lists in Python 
A built-in data type that stores set of values 
It can store elements of different types (integer, float, string, etc.) 
marks = [87, 64, 33, 95, 76]   #marks[0], marks[1].. 
student = ["Karan", 85, "Delhi"] #student[0], student[1].. 
student[0] = "Arjun" #allowed in python 
len(student) #returns length

marks=[23,34,545,666,436]
print(marks[3:4])

#### LIST 
list = [2, 1, 33,44] 
        list.append(4) #adds one element at the end [2, 1, 3, 4] 
        list.sort() #sorts in ascending order [1, 2, 3] 
        list.sort(reverse=True) #sorts in descending order [3, 2, 1] 
        list.reverse() #reverses list [3, 1, 2] 
        print(marks.insert(index, element)) #insert element at index 
        List.remove()
        list.pop(index)
        print(list)

Tupples # most used 
my_tuple = (1, "hello", 3.14,1)
print(my_tuple.index(1))
print(my_tuple.count(1)) 

### Dictionary & sets
Dictionary in Python Dictionaries are used to store data values in 
 Dictionaries are unordered
key:value pairs They are unordered, mutable(changeable) & don't allow duplicate keys 
dict = { "name": "shradha", "cgpa": 9.6, "marks" : [98, 97, 95], "key" : value } 
dict["name"], dict["cgpa"], 
dict["marks"] dict["key"] = "value"   #to assign or add new
#### student = {"name" : "Alice", "age": 25, "courses": ["Math", "Science"]}
print(student["name"])

Dictionary Methods
myDict.keys() #returns all keys 
myDict.values() #returns all values 
myDict.items() #returns all (key, val) pairs as tuples
myDict.get("key"") #returns the key according to value 
myDict.update(newDict) #inserts the specified items to the dictionary

Sets:
in Sets duplicate values are not allowed
my_set = {3, 1, 4, "hello world"}
print(my_set)  # Output could be: {1, 3, 4}
 set.add(): Adds an element to the set.
set.remove(): Removes an element. Raises an error if the element does not exist.
set.discard(): Removes an element but does not raise an error if the element does not exist.
set.clear(): Removes all elements from the set.
set.pop(): Pop element in set 
print(my_set)
 collection = set() # to deploy the empty set

sets are mutable(changeable) and their value are immutable(non-changable)

Set Methods 
set.union(set2) #combines both set values & returns new 
set.intersection(set2) #combines common values & returns new

Chapter 5 : LOOPs
repeat instruction for , while

# count = 0
while count < 5:
    print(count)
    count += 1

Break and continue

Break:
Exits the loop completely when encountered.
Useful when you want to stop the loop early.

for i in range(5):
    if i == 3:
        break  # Stops the loop when i is 3
    print(i)

Continue:
Skips the current iteration and moves to the next one.
Useful when you want to skip certain values.

for i in range(5):
    if i == 3:
        continue  # Skips printing when i is 3
    print(i)

For Loop with Else:
The else block runs after the loop completes all iterations unless the loop is interrupted by a break.

# for i in range(3):
    print(i)
else:
    print("Loop is done")

Range 
The range() function generates a sequence of numbers and is commonly used in for loops.
range(start, stop, step)    # step: (Optional) The difference between each number. Default is 1

for i in range(1, 10, 2):
    print(i)                     # output: 1 3 5 7 9

pass Statement in Python (Short Notes)
The pass statement is used as a placeholder for code that you don’t want to execute or hasn’t been written yet.

# for i in range(5):
    if i == 3:
        pass  # No action for 3, but the loop continues
    else:
        print(i)


## Chapter - 6 -- function and recursion
def greet(name):
    print(f"Hello, {name}!")
greet("Alice")

## End Function:
print("Hello", end=" ")
print("World")

Recursion
# when a function call its self repeatidly
def fibonacci(n):
    if n <= 1:  # Base cases: F(0) is 0, F(1) is 1
        return n
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)  # Recursive calls
print(fibonacci(34))  # output 5702887

recursive function I 
def show(n):
        if (n == 1):   #Base case which is important to execute other wise it will be 
                return  #continue at the level when the memory crases and code would be close
        print(n)
        show(n-1)
        print(n)
show (4)

########### Chapter 7 File I/o

OPENING A file
The open() function is used to open a file.
## file_object = open("filename", mode)
"r": Read (default mode).
"w": Write (overwrites the file if it exists or creates a new file).
'x' : CREATE A new file and ope it for writing
 '' 
Example : 
file = open("D:\\Addapi_custom\\reverse geocode\\sample\\Book1.csv", "r")  # Open for reading
print(file)

Reading a file
data.read()
data.readline() ## to read a particular line in data 

# # Example - Reading only
file = open("C:\\Users\\CE00161524\\Desktop\\VsChirag\\1Abc\\demo.txt","r")
data=file.read(88)
print(data)
file.close()

## Writing to a file
E-1
f= open("C:\\Users\\CE00161524\\Desktop\\VsChirag\\1Abc\\demo.txt","w")
f.write("Overwriting") #overwrites the entire code

# E-2
f= open("C:\\Users\\CE00161524\\Desktop\\VsChirag\\1Abc\\demo.txt","a")
f.write("\n Add new thing in file ") #Addd to the file  # * It can also create new file #

Link of stack overflow: https://stackoverflow.com/questions/1466000/difference-between-modes-a-a-w-w-and-r-in-built-in-open-function 

## "With" Syntex
with is for file handling, where it automatically closes the file after the block of code is executed.
same work as to read or write the data in file

with open("C:\\Users\\CE00161524\\Desktop\\VsChirag\\1Abc\\demo.txt", "w") as file:
    content = file.write("Content")
    print("content")

## Delelting the file:  Using OS model ,, Module (like a code library) is a file written by another programmer that generally has a functions we can use.
pip3 install tensorflow
Import os
os.remove(filename) 

## Object Oriented programming
class and object in programming
class is a blue print for creating object
# E-1
class Car:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

Object
Define the Car class
Example

class Car:
    def __init__(self, make, model):
        self.make = make
        self.model = model
    def display_info(self):
        print(f"Car: {self.make} {self.model}")
# Instantiate an object of the Car class
my_car = Car("Tesla", "Model S")   # object 
# Call the method to display car information
my_car.display_info()  # Outputs: Car: Tesla Model S

### __init__ functionality
constructor
All classes have a function called_init_(), which is always executed when the class is being initiated.
Creating class and Creating object

Syntex:
class ClassName:
    def __init__(self, attribute1, attribute2):
        self.attribute1 = attribute1
        self.attribute2 = attribute2

Example--
class Person:
        # Default should be their with pass
    def __init__(self, name, age):   # take the self 
        self.name = name
        self.age = age
    
 # Parameterized constructor      
    def greet(self):
        print(f"Hello, my name is {self.name} and I am {self.age} years old.")
# Creating an object of the Person class
person1 = Person("John", 30)
person1.greet()


Class and instance attributes
        class.atr
        obj.attr


-------------------------------------------------------------------------------------------------------------------------------------
OOPS -2
11111111111111 
Del
class student:
        def __init__(self, name):
                self.name = name
s1=student("Chirag")

del s1
print(s1)

2222222222222222222
private (like) attributes & methods

class account:
        def __init__(self, acc_no, acc_pass): # we can also use __ for private also
                self.acc_no = acc_no
                self.__acc_pass = acc_pass  # __ is to make the private
        def reset_pass(self):
                print(self.__acc_pass)
                
acc1 = account("12345","abcde")

print(acc1.acc_no)
print(acc1.__acc_pass)

333333333
public and private
class person:
        __name = "anonymous"
        
        def __hello(self):
                print("hello person")
        def welcome(self):
                __hello()
p1 =person()
print(p1.welcome)


4444444444444
Inheritance when one child class inherit the properties of its parent class
class car and class toyota_car

class car:
        color = "black"
        @staticmethod
        def start():
                print("car start....")
        
        @staticmethod
        def stop():
                print("car stopped")

class toyotacar(car):
        def __init__(self,name):
                self.name =name
car1 = toyotacar("fortuner")
car2 = toyotacar("bugati")

print(car1.name)
print(car1.color)

# 444444444444444444
# 3 types of inhertance:
# single inheritance: A class inherits from one base class
# multi-level inheritance: A class inherits from more than one base class.
# multiple inheritance: A class inherits from a derived class (creating a chain of inheritance).

# single inhertance:
class car:
        color = "black"
        @staticmethod
        def start():
                print("car start....")
        
        @staticmethod
        def stop():
                print("car stopped")

class toyotacar(car):
        def __init__(self,name):
                self.name =name
car1 = toyotacar("fortuner")
car2 = toyotacar("bugati")

print(car1.name)
print(car1.color)

multilevel inhertance
class car:
        color = "black"
        @staticmethod
        def start():
                print("car start....")
        
        @staticmethod
        def stop():
                print("car stopped")

class toyotacar(car):
        def __init__(self,name):
                self.name =name
                
class fortuner(toyotacar):
        def __init__(self,type):
                self.type = type                
                
car1 = toyotacar("diesal")
car1.stop()

5555555555 
# Multiple Inhertance
class a:
        vara ="welcome to class A"
class b:
        varb="welcome to class B"
class c(a,b):
        varc = "welcome to class c"
c1=c()
print(c1.vara)
print(c1.varb)
print(c1.varc)
        
# 66666666666666666666
# super method: super() method is used to access method of parent class
# super ka matlab parent (inherit)

class car:
        def __init__(self,type):
                self.type =type        
        
        @staticmethod
        def start():
                print("car start....")
        
        @staticmethod
        def stop():
                print("car stopped")

class toyotacar(car):
        def __init__(self,name,type):
                self.name =name
                super().__init__(type)
                super().start()
                                             
car1 = toyotacar("prius","electric")
print(car1.type)

# 77777777777777
class method : A class method is bound to the class & receives the class as an implicit first argument. Note - static method can't access or modify class state & generally for utility.
class Student: 
       @classmethod #decorator 
       def college(cls): 
                   pass
----------------------------------------------------
class person:
        name="anonymous"
        
        # def changename(obj, name):
        #         self.__class__.name = "Rahul"
        @classmethod
        def changename(cls,name):
                cls.name=name
        
p1 =person()
p1.changename("rahul kumar")
print(p1.name)
print(person.name)

# # Notes:
# methods:
#         staticmethod()
#         classmethod(cls)
#         instancemethod(self)

# 88888888888888888
property decorator: We use @property decorator on any method in the class to use the method as a property.

class student:
        def __init__(self,phy,chem,math):
                self.phy = phy
                self.chem = chem
                self.math = math
        
        @property
        def percentage(self): 
                return str((self.phy + self.chem + self.math) / 3) + "%" 
        
stu1 = student (98, 97, 99) 
print(stu1.percentage) 

stu1.phy = 86 
print(stu1.percentage)
        
# deocorator : getter(),setter()
## 99999999999999999999999999
# Polymorphism: When the same operator is allowed to have different meaning according to the context.
# a+b,-,*,/,%(mod)

# 
class complex:
        def __init__(self,real,img):
                self.real = real
                self.img = img
        
        def shownumber(self):
                print(self.real,"i +",self.img,"j")
                
        def add(self, num2):
                newreal=self.real + num2.real
                newimg = self.img +num2.img
                return complex(newreal, newimg)
num1=complex(1,3)
num1.shownumber()

num1=complex(4,6)
num1.shownumber()

# The End
