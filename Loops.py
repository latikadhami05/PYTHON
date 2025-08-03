# LOOPS in python
# loops are used to repeat instructions
# while loops-
# while condition:
        # some work
        
#for infinite looop ( kyuki TRUE to haemsha rahega)
    #while True:
    #print("hello")

#not cant infinite so , 5 times hello word
count = 1   # count is iterator
while count <=5:
    print("hello")
    count += 1
print(count)

#same could be written as-
i=1  # here i is iterator
while i <= 10:
    print("apnacollege",i)
    i+=1

#print numbers 1 to 5
i=1
while i<=5:
    print(i)
    i+=1
    
print("loop ended")
    
# print the reverse i.e 5 to 1
i=5
while i >= 1:
    print(i)
    i -=1
print("end if this")
# BREAK : used to terminate the loop when encountered.
# CONTINUE: terminates execution in the current iteration & continues execution of the loop with the next iteration
i = 1
while i <= 5:
    print(i)
    if(i==3):
        break
    i += 1
print("end of 1st break")

nums=(1,4,9,16,25,36,49,64,81,100)

x = 36

i = 0   #initialisation
while i < len(nums):
    if(nums[i] == x):
        print("FOUND at idx",i)
        break
    else:
        print("finding..")
    i+= 1
print("end of 2nd break")

i=0
while i<=5:
    if(i==3): #bss 3 print nhi hoga
        i += 1
        continue # iske wala #SKIP
    print(i)
    i += 1
print("end of 1st continue example")

#for printing the odd number ( by using continue for skipping the even numbers)
i=0
while i<=10:
    if(i%2==0): # even wale skip ho jayenge coz using CONTINUE
        i += 1
        continue #SKIP
    print(i)
    i += 1
print("end for the odd ones ")


# for printing the even  numbers
i=0
while i<=10:
    if(i%2!=0): # odd wale skip ho jayenge coz using CONTINUE
        i += 1
        continue #SKIP
    print(i)
    i += 1
print("end for the even ones ")