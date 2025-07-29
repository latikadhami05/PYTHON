# INCLUDE PRACTISE QUESTIONS OF TOPICS-
# DICTIONARY , SETS 

# Q1. Store following word meanings in a python dictionary:
#     table:"a piece of furniture","list of facts & figures"
#     cat:"a small animal"
dictionary = {
      "cat":"a small animal",
      "table": ["a piece of furniture ","list of facts & figures"]
      # table has 2 values so had to store it in form of tupe or list --{} or []
  }
print(dictionary)


# Q2. You are given a list of subjects for students.Assume one classroom is required
# for 1 subject.How many classrooms are needed by all students.
# "python","java","C++","python","javascript"
# "java","python","java","C++","C"
subjects={
  "python","java","C++","python","javascript",
  "java","python","java","C++","C"
}
#print(subjects)
print(len(subjects))


#Q3. WAP to enter marks of 3 subjects from the user and store them in a dictionary.
#   Start with an empty dictionary & add one by one.Use subject name as key & marks as value.
marks={}

x=int(input("enter phy: "))
marks.update({"phy" : x})

x=int(input("enter math: "))
marks.update({"math" : x})

x=int(input("enter chem: "))
marks.update({"chem" : x})

print(marks)


#Q4. Figure out a way to store 9 & 9.0 as separate values in the set.( You can take help of built-in-data types)
values={9,"9.0"} #--- if values=(9,9.0) then ans. woylf be 9 only coz pyhton take 9.0 as 9 only
print(values) 
#now using built in data type- 9 is int and 9.0 is float
values={
  ("float",9.0),
  ("int",9)
}
print(values)