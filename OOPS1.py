# mostly theoretical:

#CLASS & OBJECTS IN PYTHON
# class is a blueprint for creating objects.
# creating a class=
class Student: # always capital S for studnet ( always capital letters for classs)
    name="karan kumar"
# creating object (instance) =
s1 = Student()
print(s1.name)

s2 = Student()
print(s2.name)

#new class example:
class Car:
    color="blue"
    brand="mercedes"
    
car1=Car()
print(car1.color)
print(car1.brand)
    
    
# __INIT__ FUNCTION
# CONSTRUCTOR:
# All classes have a function calles __init__(), whixh is always executed when the object is being initiated.

# creating class  =                           #creating object
# class Student:                                # s1 = Student("karan")
    #def __init__(self,fullname):               #print(s1.name)
    #  self.name = fullname
    
    
# * the self parameter is a reference to the current instance of the class , and is used to access varible that belongs to the class"
class Student:
    college_name="abc college"
    # two types of contructors
    #1. default constructors  (jisme ek hi pararamter ho - ie self , ye nhi likha too to python apne aap hi man lega pehle parameter)
    def __init__(self):
        pass #pass hai too ye code chaleag hi nhi , upar wala constructor wont print in the terminal
    #2. parameterized constructor : ( vo constructor jisme self kai alawa aur bhi parameters hoo ,, exampple : name/fullname , marks etc.)
    def __init__(self, fullname ,marks): #constructor create kiya usme arguments daale i.e self & fullname
        self.name = fullname
        self.marks= marks
        print("adding new student in Database..")

s1=Student("latika dhami",97)
print(s1.name, s1.marks)  #latika dhami

s2=Student("divyansh" , 88)
print(s2.name,s2.marks)
print(s2.college_name)

 # data and varibles are called attributes.
 # CLASS & INSTANCE ATTRIBUTES :
 # class.attr   &   obj.attr
 
# METHODS:
# methods are functions that belong to objects.
# CREATING CLASS --                        #CREATING OBJECT--
# class Student:                             #S1 = Student("karan")
    #def __init___(self,fullname):           #s1.hello()
        #self.name=fullname
    #def hello(self):
    #print("hello",self.name)
    
#method banate hai - welcome naam ka ( with a self parameter):
print("methods example::::::::::::::::::")
class Student:
    college_name="abc college"
    
    def __init__(self,name,marks):
        self.name = name
        self.marks = marks
        
    def welcome(self): #welcome naam ka method ( with a self parameter)
        print("welcome student,",self.name)
        
    def get_marks(self): #another method named marks
        return self.marks
        
s1 = Student("karan",78)
s1.welcome()
print(s1.get_marks())


# STATIC METHODS :
# methods taht don't use the self ("self")parameter ( work at class level)
# class Student:
    # @staticmethod    #decorator
    #def college():
        #print("ABC College")
        
# ** Decorators allow us to wrap another function in order to extend the behaviour of the wrapped function, without permanently modifying it .
print("STATIC methods example TO PRINT HELLO::::::::")
class Student:
    def __init__(self,name,marks): #constructor banaya
        self.name=name
        self.marks=marks
        
            
    #to make hello() print without error it shoukd be hello(self ) but t here is no use of self her , so to make it error free we will use static method , by writing @staticmethod ( which is a decorator)
    @staticmethod
    def hello():
        print("hello") # just see last line of code now
        
        
    def get_avg(self):  #method
        sum=0
        for val in self.marks: #niche likhi list ka sum calcuate kiya
            sum += val
        print("hi",self.name,"your avg score is:",sum/3)
        
s1 = Student("tony stark", [99,98,97])
s1.get_avg()
s1.hello()



# IMPORTANT :
# ABSTRACTION : hiding the implementatio details of a class and only showing the essential feautures to the user.
# ENCAPSULATION : Wrapping data and functions into a single unit (object).

print("example of abstraction:::")
class Car:
    def __init__(self):
        self.acc = False # abhi accelerator dabaya nhi starting mai too - false
        self.brk = False # abhi break dabaya nhi starting mai too - false
        self.clutch = False # abhi clutch dabaya nhi starting mai too - false
    #ab gaadi start ki:
    def start(self):
        self.clutch = True
        self.acc = True
        print("car started ... ")
        
        #ye jo upar jitna codee likhe ha ye thodi na kahi print hoga (its uneceesaary details), this is everythoung whch is hidden or done in the background this is called abstraction.
car1 = Car()
car1.start()


