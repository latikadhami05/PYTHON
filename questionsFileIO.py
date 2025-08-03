# FILE INPUT OUTPUT QUESTIONS

# Q1. Create a new file "practise.txt" using python. Add the following data in it :
#     Hi everyone
#     we are learning File I/O
#     using Java.
#     I like programming in Java.
with open("practice.txt","w") as f:
    f.write("Hi everyone\nwe are learning File I/O\n")
    f.write("using Java.\nI like programming in Java.")



#Q2. WAP that replace all occurences of "java" with "python" in above file.
with open("practice.txt","r") as f:
    data = f.read()
#to replace in this fle output terminal:
new_data = data.replace("Java","Python")
print(new_data)
# to replace in the practise.txt file:
with open("practice.txt","w") as f:
    f.write(new_data)



#Q3. Search if the word "learning" exists in the file or not.
# waf - write a function:
def check_for_word():
    word="learning"
    with open("practice.txt","r") as f:
        data = f.read()
        if(word in data):
            print("found")
        else:
            print("not found")
            
check_for_word()


#Q4. WAF to dind in which line of the file does the word "learning" occur first. Print -1 if word not found.
def check_for_line():
    word = "learning"
    data = True
    line_no = 1
    with open("practice.txt","r") as f:
        while data:
            data = f.readline()
            if(word in data):
                print(line_no)
                return
            line_no += 1
            
    return -1

check_for_line()


#Q5. From a file contaning numberss separated by comma ,print the count of even numbers.
count = 0 
with open("practice1.txt","r") as f:
   data = f.read()
   
   nums = data.split(",")
   for val in nums:
       if(int(val)%2==0):
           count += 1
print(count)
# out of 1,2,76,84,90,101 --- four are even out of this ie 2,76,,84,90