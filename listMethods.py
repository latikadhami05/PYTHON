list=[2,1,3]

print(list.append(4)) #adds one element at the end (2,1,3,4)
print(list.sort()) #sorts in ascending order (1,2,3)
print(list.sort(reverse=True)) #sorts in descending order (3,2,1)
print(list.reverse()) #reverse list (3,1,2)
#print(list.insert(idx,el)) #insert element at index
print(list)

#all get none

list.insert(1,5)
print(list)

# list= [2,1,3,1]
# list.remove(1) -- removes first occurence of elements- [2,3,1]
#list.pop(idx)-- removes element at idx

list.pop(2)
print(list)
