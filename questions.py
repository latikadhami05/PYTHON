# QUESTIONS FROM TOPICS-
# VARIABLES,DATA TYPES,STRINGS & CONDITIONAL STATEMENTS
# LISTS AND TUPLES


#wap to input user's first name & print its length
name= input("first name: ")
print(len(name))

#wap to find the occurence of '$' in a string
str="thi$ i$ a $tring replacing the s with $ in thi$"
print(str.count("$"))


#wap to check if a number entered by the user is odd or even
num= int(input("enter a number: "))
if(num%2==0):
    print("EVEN")
else:
    print("ODD")
    
    
#wap to find the greater of 3 numbers entered by the user
a=int(input("a = "))
b=int(input("b = "))
c=int(input("c= "))
if(a>=b & b>=c):
    print(" a is greatest",a)
elif( b>=c):
    print("b is greatest",b)
else:
    print("c is greatest",c)
    

#wap to check if a number is a multiple of 7 or not
num=int(input("the number="))
if (num%7==0):
    print(num,  "is multiple of 7")
else:
    print(num, "not multiple")


#wap to ask the user to enter names of their 3 favourite movies and store them in a list
movies=[] #let it be empty list first
mov1=input("enter 1st movie:")
mov2=input("enter 2nd movie:")
mov3=input("enter 3rd movie:")

movies.append(mov1)
movies.append(mov2)
movies.append(mov3)

print(movies)

# another method for this-
movies=[] 
mov=input("enter 1st movie:")
movies.append(mov)
mov=input("enter 2nd movie:")
movies.append(mov)
mov=input("enter 3rd movie:")
movies.append(mov)

print(movies)

# one another method-
movies=[]
movies.append(input("enter 1st movie:"))
movies.append(input("enter 2nd movie:"))
movies.append(input("enter 3rd movie:"))
print(movies)

#WAP to check if a list contain a palindrome of elements.
# [1,2,3,2,1] and # [1,"abc","abc",1]
# palindrome - shuru sai aur akhri sai same padhte hai usee- to check logic - uska reverse and original to be same
# example- racecar , maam
list1=[1,2,1] #list1=["m","a","a","m"]
list2=[1,2,3]
copy_list1=list1.copy()
copy_list1.reverse()

if(copy_list1==list1):
    print("palindrome")
else:
    print("NOT PALINDROME")


#WAP to count the number of students with the "A" grade in the followin tuple
# ["c","D,A,A,A,B,B,A"]
# store the above values in a list & sort them from "A" to "D"
grade=["C","D","A","A","B","B","A"]
print(grade.count("A"))
grade.sort()
print(grade)
