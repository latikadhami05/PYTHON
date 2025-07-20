# LISTS
# lists is a builit-in data type that stores set of values 
# it can store elements of different type( integer, float,string , etc.)
# marks=[87,64,33,95]  -- marks[0],marks[1],......

marks=[94.4,87.5,95.2,66.4,45.3]
print(marks)
print(type(marks))
print(marks[0]) #printing marks of 0th index 
print(marks[1]) #1th index

# strings are- immutable ( in python)( cann0t be changed)
#lists are- mutable ( in python) (can be changed)

student=["latika", 95.4,"delhi"]
print(student[0])
student[0]="arjun"  # lists are mutable
print(student)


# LIST SLICING
# similar to string slicing
# list_name[starting_idx : ending_idx] -- ending idx is not included
marks1=[85,93,32,43,48]
print(marks[-3:-1]) #negative slicing
print(marks[:4]) # is same as marks[0:4]
print(marks[1:]) #is same as marks[1:len(marks)]
