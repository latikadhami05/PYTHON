#FUNCTIONS IN PYTHON
# Functions is a block of statement that perform a specific task.

# Function Definition:
# def func_name(param1,param2..):  -- def means define
#      # some work
#       return val
# func_name(arg1,arg2...)--# fucntion call

def calc_sum(a,b):
    sum=a+b
    print(sum)
    return(sum)
#now we can use this for 3 calculations all together:
calc_sum(5,10)
calc_sum(12,17)
calc_sum(2,10)

# now to summarise this:
def calc_sum(a,b): # fucntion definition , a and b are parametrs
    return(a+b)

sum=calc_sum(5,10) # function call ; 1,2 are arguments which are then stored in the paramters( which are a,b here)
print(sum) 

# to print hello as manyy times...
def print_hello():
    print("hello")

print_hello()
print_hello()
print_hello()
print_hello()#... kitne baar bhi hello print hoga jitne baar we will write print_hello()


# ab ye print_hello ka output store kar raha hai, aur isi output ko ham print karwa rahe hai
# to print hoga - none , kyu? - kyuki jo function return (return hello aise)mai kuch return nhi karta uske output mai automatically none value aa jati haii
output=print_hello()
print(output)  #none

#average of 3 number =
def calc_avg(a,b,c):
    sum=a+b+c
    avg=sum/3
    print(avg)
    return avg
calc_avg(1,2,3)
calc_avg(33,63,45)

# TW0 TYPES OF FUNCTIONS-
#1. Built-in Functions- print(),len(),type(),range()
#2. User defined Functions

# DEFAULT PARAMETERS
# -- Assigning a default value to paramater, which is used when no argument is passed.
def cal_prod(b,a=2):
    print(a*b)
    return a*b
cal_prod(3) # here we got value of 3 ( coz b,a=2) so b*2=3*2=6 output


# RECURSION
# -- when a function calls itself repeatedly
# jo saare problems ham loop sai karte hai vo recursion sai leye jaa sakte , aur jo recusrsion sai kaam kiye jaate voo loop sai bhi lieye jaa sakte 
# loops and recursion are interlinked

print("recursion problem 1: ") #we want to print 5,4,3,2,1 but not with loop but wuth recursion
def show(n):
    if(n == 0):  # this is base case - id (n== -1) too 5 sai 0 tak print ho jata
        return
    print(n)
    show(n-1)
    
show(5) # now 5 , 4 = n-1, 3= n-2, 2= n-3 ,1


print("recursion problem 2 : ")
def fact(n):
    if( n == 0 or n==1):
        return 1
    else:
        return n * fact(n-1)  # logic :
    # n! = (n-1)! * n    ----  ( fact (n-1) x return n)
    # 5! = 4! x 5
    # 4! = 1 x 2 x 3 x 4 = 3! x 4
    # 3! = 1 x 2 = 2! x 3
    
print(fact(4))
print(fact(6))
