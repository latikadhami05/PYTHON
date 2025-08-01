A,B=2,3
Txt="@"
print(A*Txt*3) #for 6 times @ print- @@@@@@

a,b="2",3
Txt="&"
print((a+Txt)*b)

a,b=2,6
c=5
print(a+b*c)

a,b=10,5.0
c=a*b 
print(c)

#5 rule - resukt of diving 2 integers will be in float value
a,b=1,2
c=a/b 
print(c)

a,b=1.5,3
c=a//b  #1.5/3 = 0.5 ka 0.0 show hota starting ki value in c - floor number ( closest integer nikalta for c - a//b)
print(c, a/b)


#remainder is negative when denominator is negative ( otherwise all case positive)
#see following cases remainder
a,b=5,-2
c=a%b 
print(c)

#now cases of positive remainder
a,b=-5,2
c=a%b 
print(c)

a,b=5,2
c=a%b 
print(c)

#input in python
#string input
name=input("name: ")
print(name)

#int input
age=int(input("age: "))

#float input
price=float(input("price :"))

print("my name is", name, "and I am" ,age,"years old")




