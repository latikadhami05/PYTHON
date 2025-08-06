# OOPS PART 2 OF THE LECTURE :
# DEL KEYWORD: used to delete object properties or obh=ject itself.
# del s1.name   &   del s1
print("delete keyword example: ")
class Student:
    def __init__(self, name):
        self.name = name

s1 = Student("shradhaa")
print(s1.name)
# del s1.name
print(s1.name)
# why i comment out the delete thing ? coz , we first will print shardha then will delete it , then  if we want to print shardha it wont print becoz we deleted and 
# it will get error soo this is how dlete operation work , now i dont want error in terminal so ya


#  PRIVATE(LIKE) ATTRIBUTES & METHODS:
# Conceptual Implementations in Python: Private attributes and methods are meant to be used only within the class and are nor accesible from outsidde the class.
# tehre are public and private , now wee want account password to be private , so we will change from self.acc_pass to self.__acc_pass ( . kai baad double dash laga diya to make it private):
print("private example : ")
class Account:
    def __init__(self, acc_no , acc_pass):
        self.acc_no = acc_no
        self.acc_pass = acc_pass
        self.__acc_pass = acc_pass
        
    def reset_pass(self):
        print(self.__acc_pass)
        
acc1 = Account("12345","abcde")

print(acc1.acc_no)
print(acc1.reset_pass()) # isse error nhi ayegaa

# private jaisa hota hai python mai , private nhi -- aur private jaisa karna ka ek hi tarika to put (_ _) infront of both attrubutes and methods


# INHERITANCE :
# when one class (child/derived) derives the properties & methods of another class (parent/base)
# class Car:
   # ....
# class ToyotaCar(Car):
   #....
print("INHERITANCE EXAMPLE ::::")
class Car:
    color = "black"
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")
    
class ToyotaCar(Car):
    def __init__(self,name):
        self.name = name
        
car1 = ToyotaCar("fortuner")
car2 = ToyotaCar("prius")

print(car1.start())
print(car1.name)
print(car1.color)
    
# TYPES OF INHERITANCE : single inheritance , multi-level inheritance , multiple inheritance
print("MULTILEVEL  INHERITANCE EXAMPLE : ")
# example by using brand name - varous brand kai leye class (jaise class fortuner brand ki etc.) banayenge :
class Car:
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")
    
class ToyotaCar(Car):   # CAR ki saari properties TOYOTA CAR lee gaya
    def __init__(self,brand):
        self.brand = brand  #brand ka 

class Fortuner(ToyotaCar):    #fortuner brand ki class ( ab toyota car kai brand kaa fortuner lega propetries , its multilevel inheritance car sai toyota , toyota sai fortuner pai)
    def __init__(self,type):
        self.type = type # type ko store kar diya 

car1 = Fortuner("diesel")
car1.start()


# MUTIPLE INHERITANCE ( 2 BASE CLASS KA EK HI INHERITED KAR RAHA DERIVED CLASS -- 2 parent 1 child):
print("MULTIPLE INHERITANCE EXAMPLE :::::::::")
class A:
    varA = "welcome to class A"

class B:
    varB = "welcome to class B"
    
class C(A,B):
    varC = "welcome to class C"

c1=C()

print(c1.varC)
print(c1.varB)
print(c1.varA)


# SUPER METHOD -- super() method is used to access methods of the parent class.
print("SUPER() METHOD EXAMPLE --- ")
class Car:
    def __init__(self,type):  # class kai andar ye contructor define kya jisme ham type lenge
        self.type = type   #   --eq(1)
        
    @staticmethod
    def start():
        print("car started..")
    
    @staticmethod
    def stop():
        print("car stopped..")
    
class ToyotaCar(Car):  
    def __init__(self,name,type):
        self.name = name
        super().__init__(type) # super()matlab parent , (type) dalke in super hamne toyota car mai eq(1) kai contructor ki properties kai type method ko isme inherit kar diyaa (typoe method kooo)
        #super class kai andar constructor (init) call ho jayega jisme type method already chale gaya
        
car1 = ToyotaCar("prius","electric") #electric is typpe
print(car1.type)


# CLASS METHOD ::
# A class method is bound to the class & receives the class as an implicit first argument.
# Note-- static method can;t access or modify class state & generally for utility.
# class Student:
    # @classmethod   #decorator
    #def college(cls)
        #pass
print("class method example:")
class Person:
    name = "anonymous"
    
    @classmethod  # isse direct we can acces to class person pai (cls)
    def changeName(cls,name):
        cls.name=name
        
p1 = Person()
p1.changeName("rahul kumar")
print(p1.name)
print(Person.name)

# PROPERTY :-- we use @property decorator on any method in the class to use the method as a property.
print("property example ::")
class Student:
    def __init__(self,phy,chem,math): # contructor kai andar subjects
        self.phy = phy
        self.chem = chem
        self.math= math
        
    # ek percentage attribute banana thaa  to yaha banaya--
    #def calcPercentage(self):
        #self.percentage = str((self.phy + self.chem+self.math) /3) + "%"
        # isi same kaam ko karne ka ek aur tarika--
        
    @property
    def percentage(self):
        return str((self.phy + self.chem+self.math) /3) + "%"
    
stu1 = Student(98,97,99)
print(stu1.percentage)

stu1.phy = 86  #ye change karana too phir prepert attribute lenge
print(stu1.percentage)


# POLYMORPHISM : operator overloading
# when the same operator is allowed to have different meaning accoording to the context . 

# OPERATORS & DUNDER FUNCTIONS : (dunder functions are those jiske age hamye 2 - _ _ lagate haii)
#  a+b  # addition               a._ _ add _ _ (b)
#  a-b  # subtraction            a._ _ sub _ _ (b)
#  a*b  # multiplication         a._ _ mul _ _ (b)
#  a/b  # division               a._ _ truediv _ _ (b)
#  a%b  # remainder              a._ _ mod _ _ (b)

print(1+2) #3
print(type(1))

print("apna"+"college")  # concatenation
print(type("apna"))

print([1,2,3] +  [4,5,6]) # merge
print(type([1,2,3]))

# now ab ye chiz ham classs mai kar sakte 
# complex number = 5i + 6j ( real+imaginary )
print("complex number == ")
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i+", self.img, "j")
        
    def add(self,num2):  #-- equation 2
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
        
        
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()
# now we need to add these two complex number of -- num1 + num 2 basically ( 1i+3j)+ (4i+6j) = (5i+9j)
# soo go to equstion 2. then to num 3
num3=num1.add(num2)
num3.showNumber()

# BUT WE WANTED LIKE THIS NUM3=NUM1+NUM2 , BUT IUT WILL GIVE ERROR SO INTEAD WE WILL USE OPEARTORS AND DUNDER FUCNTIONS
# nowwww
print("OPERRATOR OVERLOADING / polymorphism implementation--")
print("dunder fucntion using in complex numbers : (with same output as before)")
class Complex:
    def __init__(self,real,img):
        self.real = real
        self.img = img
        
    def showNumber(self):
        print(self.real,"i+", self.img, "j")
        
    def __add__(self,num2):  #-- see this -- using dunder function
        newReal = self.real + num2.real
        newImg = self.img + num2.img
        return Complex(newReal,newImg)
    
    #for subtraction too ---
    def __sub__(self,num2):  #-- see this -- using dunder function
        newReal = self.real - num2.real
        newImg = self.img - num2.img
        return Complex(newReal,newImg)
        
        
num1 = Complex(1,3)
num1.showNumber()

num2 = Complex(4,6)
num2.showNumber()

num3=num1+num2 #-- now this will not give error coz used dunder function:
num3.showNumber()

num4=num1-num2 # subtrraction
num4.showNumber()

