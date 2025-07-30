#conditional statements practise
# syntax:
#  if(condition):
# ( 4 spaces kai baad) Statement 1 ( called INDENTATION - proper spacing)
# elif(condition2):
#    statement2
#else:
#    statementN

light=input("light = ")
if( light=="red"):
    print("stop")
elif(light=="yellow"):
    print("look")
elif(light=="green"):
    print("go")
else:
    print("light is broken")
    
    
# single line if / Ternary Operator
# <var>=<val1>if<condition>else<val2>
food= input("food : ")
eat="Yes" if food == "cake" else "no"
print(eat)
#<stt1>if<condition>else<stt2>
food = input("food :")
print("sweet")if food == "cake" or food == "jalebi" else print("not sweet")

#clever if / Ternary Operator
#<var>=(false_val,true_val)[<condition>]
age=int(input("age : "))
vote=("yes","no")[age<18]

sal=float(input("salary: "))
tax=sal*(0.1,0.2)[sal>50000] #f,t case too agar salary 50k sa zyda too 0.2 sai multiply mai true
print(tax)


#nesting
age=34

if(age>=18):   #1 statement kai under doosri statement is nesting
    if(age>=80):
        print("cannot drive")
    else:
        print("can drive")
else:
    print("cannot drive")
