
#FUNCTIONS QUESTIONS
 
#Q1. WAP to print the length of a list (list is the parameter)
cities=["delhi","gurgaon","noida","pune","mumbai"]
heroes=["thor","ironman","captain america"]

def print_len(list): #defining a list
    print(len(list))
    
print_len(cities) # print length ko call kiya cities ka leye
print_len(heroes)


#Q2. WAP to print the elements of a list in a single line.(list is the parameter)
cities=["delhi","gurgaon","noida","pune","mumbai"]
heroes=["thor","ironman","captain america"]

def print_list(list):
    for item in list:
        print(item,end=" ") #to make it in same line end="  "

print_list(heroes)

print("next:")


#Q3. WAP to find the factorial of n.(n is the parameter)
def cal_fact(n): # defiining fucntion
    fact=1  #factorial variable banaya
    for i in range(1,n+1): #phir loop chalayenge phir loop kai andar:
        fact *= i # factorial value ko calculate karnge
    print(fact) # phir factorial ko print kara dengee

cal_fact(5) #call kiya


#Q4. WAP to convert USD to INR.
def converter(usd_val):
    inr_val = usd_val * 85.83
    print(usd_val,"USD = ", inr_val,"INR")

converter(1)
converter(3537)


# RECURSIVE FUNCTIONS PRACTISE QUESTION : 

# Q1.Write a recursive function to calculate the sum of first n natural numbers.
def calc_sum(n):
    if(n == 0):
        return 0
    return calc_sum(n-1)+n
#logic :
# sum(5)= sum(4) + 5 
# sum(4)=sum(3)+ 4
# sum(3)=sum(2)+ 3 
# pattern ---- sum(n)= sum(n-1)+ n ---- calc_sum(n-1)+ n
print("recursice practise questions : ")
sum = calc_sum(5)
print(sum)


#Q2. Write a recursive fucntion to print all elements in a list ( HINT :  use list and index as parameters.)
def print_list(list, idx=0):
    if( idx == len(list)):
        return
    print(list[idx])
    print_list(list,idx+1)
    
fruits= ["mango", "litchi" , "apple", "banana"]
print_list(fruits)
