class Student:
    grace_marks=10 # class variable
    address1=[]
    TOTAL_MARKS=100
    def __init__(self,name,marks): #it is a constructor, when object is created then its calling automaticalky
        Student.m2=4 #static member variable
        #self is a reference variable of instance(class object) and it is used to access variables that belong to class
        # when u want to initiate the variable so constructor help to initialize the variables
        self.name1=name #instance variable
        self.marks1=marks
        self.grace_marks=20 #this is instance variable
    def __del__(self):
        print("constructor is going to die now")

    def display(self): # it is a instance method, because it referred from object
        print("hi",self.name1)
        print("Your marks is",self.marks1)

    def class_grade(self):
        if self.marks1>=35:
            self.marks1 = int(self.grace_marks + self.marks1)
            print(f"we gave {self.grace_marks} grace marks","now your marks is=", self.marks1)
            if self.marks1>=60:
                print("you got 1st place with",self.marks1)
            elif self.marks1>=50:
                print("you got 2nd place with",self.marks1)
            else:
                print("you failed",self.marks1)
        else:
            print("you failed")

    def grade(self):
        return f"this is grade function={self.marks1}"

    def setAddress(self,address):
        self.address1.append(address)                        ######check when we use class method and instance method
        return self.address1 #here i used class variable

    def getAddress(self):
        return self.address1
    def GLOBAL(self):
        global var,name #here we use global keyword and it helps to take many variables and print output
        var=6
        name="rohit"
        return var,name
    @classmethod
    def cla_met(cls):
        return cls.grace_marks

# we created a main function and pass it in if __name__=="__main__"
def main():
    marks_result=int(input("enter the marks"))
    John=Student("John cena",marks_result) #object created
    John.display() #here we call display function from object
    John.class_grade()
    print(John.grade())
    print(John.setAddress("NOIDA,UP"))
    print(John.GLOBAL())
    John.TOTAL_MARKS=90 # here object has own variable is TOTAL_MARKS And its value is 90
    print(John.TOTAL_MARKS)
    #but we cannot change class variable value by its object, we can only change its class variable value by class method
    print(John.grace_marks)

if __name__ == '__main__':
    main()

# ------------------------------------------------------------
# All variables which are assigned a value in the class declaration are class variables.
# And variables that are assigned values inside methods are instance variables.
# method overlodong - method overloading is when we write two or more method with same name in same class
#method overriding- method overriding means when we write mehod with same name in the class and the inherited class
class dog:
    #class variable or Static variable
    a=6
    is_hairy=True
    #constructor
    def __init__(self,name):
        #names is a instance variable or non static variable
        self.names=name

    #instance method
    def bark(self):
        print("wuff")

bello=dog("bello")
paris=dog('paris')
print(bello.names)

class cat:
    #python does not support method overloading
    def meau(self,times=1):
        print("meau " * times)

fifi=cat()
fifi.meau(4)

# ----------------------------------------------------------------
# class Point:
#     def print_point(self):
#         return f"(%e)" % (blank.x)
#
# blank=Point()
# blank.x=5
# print(blank.print_point())
# add two numbers from *args
# -----------------------------------------
# x = 2
# y = x ^ 2
# print(("%e") % y)
# class abc:
#     def p(self, name):
#         print("hello " + name)
#         return "done"
#
#
# abd = abc()
# print(abd.p("world"))
# ===========================================================================
# write a function  called Distance_between_point that takes to points as arguments and returns distance between them
# import math
# def distance_between_points():
#     p=5
#     q=8
#     return math.dist([p], [q])
# z=distance_between_points()
# print(z)
# ===============================================================
import math
class Point:
    def Point_Blank(self):
        x = Blank.x = 6
        y = Blank.y = 8
        Distance=math.sqrt(Blank.x**2 + Blank.y**2)
        print(Distance)
        return "done"

class Rectangle:
    """here is the rectangle attributes height, width, corner"""
    pass
def find_centre(rect):
    P=Point()
    P.x=rect.corner.x + rect.width/2
    P.y=rect.cornre.y + rect.height/2

Blank=Point()
find_centre(6)
print(Blank.Point_Blank())
Box= Rectangle()
height=Box.height=4
width=Box.width=6
Box.corner=Point()
Box.corner.x=0.0
Box.corner.y=0.0
print(Rectangle.__doc__)
find_centre(400)
# ----------------------------------------------------------------------------------------------
# +++++++++++++++++++++++++++++++++++++++POLYMORPHISM++++++++++++++++++++++++++++++++++++++++++++++++++++
# _____PRIVATE____PUBLIC______PROTECTED (ACCESS MODIFIERS)
# class Specifiers:
#     # __VARIABLES__
#     pub=5 #mean everyone can use it
#     _pro=10 #mean only base class and child class can use it
#     __pri=15 #mean only class can use it, does not use inherited class
#     # __METHODS__
#     def __private_method(self):
#         return f"this is private method and with private variables {self.__pri}"
#
# obj1=Specifiers()
# print(obj1.pub)
# print(obj1._pro) #here i have to use _pro ro print because it is protected variables
# print(obj1._Specifiers__pri) #here i have to use protected variables with _classname__variablename that is called as namemangling
# print(obj1._Specifiers__private_method()) #here i have to use _class name__methodname to print private method
# # -----------------------------------------------------------------------------------
# # ______JUST AN EXAMPLE_________
# class A:
#     class_var="i am in class A"
#     def __init__(self):
#         self.class_var="this is instance variable of A"
#     def instance_method(self):
#         pass
#         #instance method
# #i can give instance variable two types first is i can pass from when we create object and
# # second is when we create instance method, use self.name="rohit"
# class B(A):
#     class_var="i am in class B"
#     def __init__(self): # here we override the constructor
#         # super().__init__() #super means it inherits the base class constrcutor
#         #when we run obB.class_var so what happen now it goes to super and check it into base class A
#         # if it's found, print then it goes next line and here is also present class_var so it prints B
#         # BUT if YOU WILL WRITE super().__init__() after class_var so it print class_var B and goes to super() base class constructor and prints it
#         self.class_var="this is instance variable of B"
#         super().__init__()
#         print(super().class_var) #here we acces class variable
#
#
# obA=A()
# obB=B()
# print(obB.class_var)
# print(obB.Instance_met("rohit"))


# here i print(ob.class_var so it print "this is instance variable" why because it find class_var variable and print its if it is found


# --------------POLYMORPHISM__________________________
# One person can work in different way eg like a customer, student, player, employee,
# EG (IN POLYMORPHIEM THERE IS A CONCEPT OF OPERATOR OVERLOADING)
# print(5+6) #here we add integer so ans is 11
# print("5"+"6") #here we add integer but convert in string so ans is 56
# BUT IN PYTHON OPERATOR OVERLOADING IS NOT POSSIBLE
# HERE WE USE MAGIC METHOD LIKE __add__()
# _______OPERATOR OVERLOADING____________________
class Employee:
    def __init__(self, name, salary, role):
        self.name = name
        self.salary = salary
        self.role = role

    def print_details(self):
        return f"the name is {self.name} and his salary is {self.salary} and his role in the company is {self.role}"

    def __add__(self, other):  # add takes only two arguments
        return self.salary + other.salary   # USe these magic or dunder method for operator overloading

    def __truediv__(self, other):
        return self.salary/other.salary

    def __repr__(self):
        return f"Employee ('{self.name}', '{self.salary}', '{self.role}')"

    def __str__(self):
        return self.print_details()


E1 = Employee("rohit", 70, "programmmer")
E2 = Employee("rohan", 60, "HR")
print(E1 + E2) #here we add objects for operator overloading but that is not possible but i can happen from dunder mathod
print(E1 / E2)
print(E1) #if your write like that so you got ouput like this(<__main__.Employee object at 0x01B41E50>) so YOU HAVE TO USE __repr__ method
print(str(E1)) #so if string method is present here so its string first and want to repr so u have to use repr in print
print(repr(E1))
print(E1.print_details())
