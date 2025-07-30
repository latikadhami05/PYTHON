# LOOPS PRACTICE QUESTIONS

# Q1.Print number from 1 to 10
i=1
while(i<= 10):
    print(i)
    i+=1
print("1 to 10 loop ended")


# Q2.Print numbers from 10 to 1
i=10
while(i>=1):
    print(i)
    i-=1

# Q3.Print the multiplication table of a number n
n=int(input("number = "))
i=1
while(i<=10):
    print(n*i)
    i+=1
print("end")


# Q4.Print the elements of the following list using a loop
# [1,4,9,25,36,49,64,81,100]
print("by while")
i=1
while(i<=10):
    print(i*i)
    i+=1

print("by loop :")
nums=[1,4,9,16,25,36,49,64,81,100]

idx=0
while idx < len(nums):
    print(nums[idx]) #num[0],nums[1],nums[2]...
    idx += 1
    
#Q5. Search for a number x in this tuple using loop:
# (1,4,9,25,36,49,64,81,100)
nums=(1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0   #initialisation
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx",i)
    i+= 1
print("question 5 end")


#FOR LOOPS QUESTION

# Q6. Print the elements of following list using a loop:
#[1,4,9,16,25,36,49,64,84,100]
nums=[1,4,9,16,25,36,49,64,84,100]
for el in nums:
    print(el) #el= element
    
#Q7. Search for a number x in this tuple using loop:
# (1,4,9,25,36,49,64,81,100)
nums=(1,4,9,16,25,36,49,64,81,100,49)
x=49

idx=0
for el in nums:
    if(el==x):
        print("number found at idx",idx)
        #break -- if pehla hi 49 milne pai band karna
    idx +=1

# QUESTIONS USING FOR & RANGE():

#Q1. Print numbers from 1 to 100
print(" print numbers from 1 to 20:  ")
for i in range (1,21): # to include 20 have to end with 21 - coz last ie 21 would not print
    print(i)

#Q2.
print(" print numbers from 20 to 1:  ")
for i in range(20,0,-1): # har baar decrease by 1 so step size -1
    print(i)

#Q3. print("multiplication table of number n")
n=int(input(" multiplication of n = "))
for i in range(1,11):
    print(n*i)

#Q4. WAP to find the sum of first n numbers.(using while)
n=7
sum=0
i=1
while i <= n:  # jab tak i ki value is less than and equal to n tabh tak sum
    sum += i
    i  += 1 # to avoud inifinite loop
print("total sum = ",sum)

#Q5. WAP to find the factorial of first n numbers ( using for)
n=5
fact = 1 # factorial to initialize with 1 , otherwise if 0 too 0 sai sabh multiply ho jayegaa
for i in range(1,n+1):
    fact *= i
print("factorial = ",fact)