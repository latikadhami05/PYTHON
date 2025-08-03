 # FILE I/O in python
 # Python can be used to perform operations on a file.( read & write data)
 
 # TYPES OF ALL FILES:
 #1.Text Files: .txt , .docx , .log , etc.
 #2. Binary Files : .mp4 , .mov, .png , .jpeg , etc .
 
 
# OPEN , READ & CLOSE FILE
# we have to open a file before reading or writing.
# f = open("file_name" , "mode")
# here , file_name -- sample.txt , demo.docx  (examples these were)
#      , mode -- r: read mode , w: write mode (examples)

# data = f.read()
#f.close()


# THIS PROGRAM IS NOT WORKING THATS WHY IN COMMENT OUT :::

f=open("D:\programs\PYTHON\demo.txt","r") # by right click on demo.txt (file) , do c0py path and paste here

# data=f.read(8)
 #print(data)

line1=f.readline()
print(line1)

line2=f.readline()
print(line2)


line3=f.readline()
print(line3)  # empty line will get pribted as in demo.txt there are only 2 lines available to get printed
 
f.close()


# CHARACTER -- MEANING
# "r"-- open for reading(default)
# "w" -- open for writing , truncating the file first
# "x" -- create a new file and open it for writing
#"a"-- open for writing, appending to the end of the file if it exists
# "b" -- binary mode
# "t"-- text mode(default)
# "+" -- open a disk file for updating (reading and writing)


# READING A FILE
#data = f.read() --- reads entire file
# data = f.readline() -- reads one line at a time


# WRITING TO A FILE ::
# 1. f = open("demo.txt","w")
#    f.write("this is a new line") --- overwrites the entire file
# 2. f = open("demo.txt","a")
#    f.write("this is a new line") ---- adds to the file

f=open("D:\programs\PYTHON\demo.txt","a")
f.write("\n I want to learn Javascript tomorrow. 123 ")
f.close()
# now if you go to demo.txt the whole thing ( i.e i am learning oython from apna college) will change from i am learnng opyhton to this that to learn javascriopt -- it happend when we useed "w" , instread of "r
# but now as we use f=open("D:\programs\PYTHON\demo.txt","a")-- it will append ,  means the line that  i want to learn javascript will be added not replaces ( like taht with "w")

# now already there no exist as such file called sample.txt before, but we can simply add it by here in code only by :
f= open("sample.txt","w") # with "a" also can do same thing
f.close()

#now abc will overwrite the line , by being in first and then the rest line of demo.txt: ( this is a sample file to -- abcs is a sample file ( see clearlt this to abcs)
# f = open("demo.txt","r++")
# f.write("abc")
# f.close()
# output -- abcs is a sample file
# see website -- stackoverflow and see difference between modes a ,a+ , w , w+ , r+ in built-in open function

# WITH SYNTAX
# with open("demo.txt", "a") as f:
#     data = f.read()
with open("D:\programs\PYTHON\demo.txt", "r") as f:
    data  = f.read()
    print(data)
    
    
# DELETING A FILE
# using the os module. Module (like a code library) is a file written by another programmer that generally has a functions we can use.
#       import os -- os meand operating system
#       os.removal(file.name)
import os
os.remove("sample.txt") # sample.txt would have been deleted now