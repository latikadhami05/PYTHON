# DICTIONARY IN PYTHON
# Dictionaries are used to store data values in key:value pairs
# they are unordered ,mutable(changeable) & dont allow duplicate keys
# "key":value

# dict={
#    "name": "latika"
#   "cgpa": 9.6,
#  "marks":[98,95,97]
#  }

info={
    "name": "latika",
    "age": 35,
    "subject": ["python","C","Java"] , # stored list
    "topic": ("dict","set"), # tuple
    "is_adult" : True,
    12 : 94.4,
 }
#print(info)
print(type(info))
print(info["topic"])

info["name"]="shardhakhapra"
print(info)

null_dict={}
null_dict["name"]="apnacollege"
print(null_dict)


#NESTED DICTIONARIES -
student={
    "name": "rahul kumar",
    "subjects": {
        "phy": 97,
        "chem": 98,
        "math":95
    }
}
print(student)
print(student["subjects"])
print(student["subjects"]["chem"])

# DICTIONARY METHODS
#1. myDict.keys()  -- returns all keys
#2. myDict.values() --returns all values
#3. myDict.items() -- returns all (key,val) pairs as tuples
#4. myDict.get("key") --returns the key according to value
#5. myDict.update(newDict)-- inserts the specified items to the dictionary




