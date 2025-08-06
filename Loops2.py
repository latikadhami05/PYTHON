# FOR LOOPS

# for el in list: ( el:element , list)
       #some work
nums=[1,2,3,4]
for val in nums:
    print(val)

veggies = ["potato", "brinjal","ladyfinger","cucumber"]
for val in veggies:
    print(val)
    
# we can use for loop for tuple also
tup= (1,2,3,4,8,9)
for num in tup:
    print(num)
print("separation")
    
#for loop in string
str="apnacollege"
for char in str:
    if (char=="o"):
        print("o found")
        break
    print(char)
else:  # agar ELSE nhi likhenge too .... END print ho jayegaa - else wala kaam break mai execute nhi hoga
    print("END")
    
    
# RANGE()

# Range functions returns a sequence of  numbers,starting from 0 by default and increments 
# (by default) , and stops before a specified number.
# range(start? , stop, step?)  -- start and step are optional , but stop is mandatory
print(range(5))

seq=range(5)
print(seq[0])
print(seq[1])
print(seq[2])
print(seq[3])
print("gap")

# isi sequence mai agar loop lagana ho too..
seq=range(5)
for i in seq:
    print(i) # ending ka print nhi hota , here 0 to 5 mai , 5 is the end part-so 5 wont be printed in the loop
    
# could have also write like this -
#  for i in range(5):
#      print(i)

# 3 ways to write range()
print(" 1st way of writing range():")
for i in range(7):  #range(stop)
    print(i)
    
print("2nd way to write range(): ")
for i in range(2,8): #range(start,stop)
    print(i)

print("3rd way to write range(): ")
for i in range(2,10,2): #range(start,stop,step - (step matlab kitne sai increase karega))
    print(i)
    
print("even numbers from 1 to 20:")
for i in range(2,20,2): # for odd number - range(1,100,2)
    print(i)
    

# PASS STATEMENT
# pass is a null statement that does nothing.It is used as a placeholder for future code.
 
 # pass bs aise hi use karte,, bss loop likha par uska kuch karna nhi to pass likhdo ,nhi to error aa sakta
 # basicaaly jab loop likha par usme baad mai kaam karna abhi nhi too just write pass to skip
for i in range(5):
    pass
print("some random work")
# u can use pass in if else statements tooo
if i<5:
    pass 