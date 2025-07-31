# input() statement is used to accept values (using keyboard) from user
input("enter your name:")
name = input("name:")
print("Welcome",name)

age=input("enter your age:")
print("I'm", age ,"years old.")

val=input("enter some value:")
print(type(val),val)

int("5")
val=input("enter some value:")
print(type(val),val)

#practise question
a=int(input("number a:"))
b= int(input("number b :"))
print("sum=" ,a+b)

#practise Q- wap to input side of square and print its area
side=int(input("side="))
area= side*side
print("area of square is :", area)

#wap to input 2 floating point numbers and print their average
a=float(input(" point number a="))
b=float(input(" point number b="))
average= (a+b)/2
print("average of number is :", average)


#wap to input 2 int numbers , a and b .print True if a is greater than or equal to b .if not print false
a=int(input("a is:"))
b=int(input("b is:"))
#print("True" )if (a>=b) else print("False")
print(a>=b)
