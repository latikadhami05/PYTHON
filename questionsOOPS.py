#LETS PRACTISE OOPS IN PYTHON QUESTIONS:

# Q1. Create student class that takes name & marks of 3 subjects as arguments in constructor. Then create a method to print the average .
class Student:
    def __init__(self,name,marks): #constructor banaya
        self.name=name
        self.marks=marks
        
        
    def get_avg(self):  #method
        sum=0
        for val in self.marks: #niche likhi list ka sum calcuate kiya
            sum += val
        print("hi",self.name,"your avg score is:",sum/3)
        
s1 = Student("tony stark", [99,98,97])
s1.get_avg()

#if we want to change name of tony stark to ironman and then calculate iron man avergae
s1.name = "ironman"
s1.get_avg()


# Q2. Create Account class wuth 2 attributes - balance & account no. Create methods for debit , credit & printing the balance.
print("QUESTION 2 :")
class Account:
    #will define contructor noe
    def __init__(self,bal,acc):
        self.balance = bal
        self.account_no = acc
        
    #debit method
    def debit(self,amount):
        self.balance -= amount #debit to balance sai hatt gaya amount
        print("Rs.",amount,"was debited")
        print("total balance = ", self.get_balance())
        
    #credit method
    def credit(self,amount):
        self.balance += amount
        print("Rs.",amount,"was credited")
        print("total balance = ", self.get_balance())
        
    #abb function banayenge which will return the final balance
    def get_balance(self):
        return self.balance
    

acc1 = Account(10000, 12345)
acc1.debit(1000)
acc1.credit(500)
acc1.credit(40000) #salary aii to credited with 40k rupees
acc1.debit(10000) # rent mai 10k gayee too minus hoo jayega balance sai 10k


# Q3. Define a Circle class to create a circle with radius r using the constructor.Define an Area() method of the class which calculates the area of the circle.
      #Define a Perimeter() method of the class which allows you to calculate teh perimeter of teh circle.
print("question 3 : ")
class Circle:
    def __init__(self,radius):
        self.radius = radius
        
    def area(self):
        return (22/7) * self.radius ** 2  #area= pi*r**2
    
    def perimeter(self):
        return 2 * (22/7) * self.radius #  perimeter = 2pi*r
        
c1 = Circle(21) # took circle ka radius as 21
print(c1.area())
print(c1.perimeter())

      
# Q4.Define a Employee class with attributes role, department & salary. This class also a showDetails() method.
     #Create an Engineer class that inherits properties from Employee & has additional attribues : name & age.
print("question 4 : ")
class Employee:
    def __init__(self,role,dept,salary):
        self.role = role
        self.dept = dept
        self.salary = salary
        
    def showDetails(self):
        print("role = ",self.role)
        print("dept = ",self.dept)
        print("salary = ",self.salary)
        
class Engineer(Employee):
    def __init__(self,name,age):
        self.name = name
        self.age = age
        super().__init__("Engineer","IT","75,000") # we are making the salary part to be fixed and also the epartment ehich is IT , AND he is engineer for sure asked in question so fixed only
        
engg1 = Engineer("Elon Musk" , 40)
engg1.showDetails()

# Q5. Create a class called order which stores item and its price . Use Dunder function _ _ gt _ _() to convey that :
     # order1 > order2 if price of order1 > price of order 2
         # gt means -- greater than
print("question 5 : ")
class Order:
    def __init__(self,item,price):
        self.item = item
        self.price = price
        
    def __gt__(self,odr2):
        return self.price > odr2.price

odr1 = Order("chips",20)  # itemm, price = chips,20
odr2 = Order("tea",10)

print(odr1 > odr2)   #true


