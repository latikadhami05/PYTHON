# SET IN PYTHON
# Set is the collection of the unordered items.
# Each element in the set must be unique & immutable.

# nums={1,2,3,4}
# set2={1,2,2,2}
# repeated elements stored only once, so ut resolved to {1,2}
# null_set=set()  -- empty set syntax

collection={1,2,2,2,4,"hello","world","world",3}
# duplicate values like 2,2,2 will be ignored to just single 2 [in set]
print(collection)
print(type(collection))
print(len(collection))  #total number of items

collection=set() #empty set; syntax
print(type(collection))

#SET METHODS
# set.add(el) -- adds an element
# set.remove(el) -- removes an element
# set.clear() -- empties  the set
# set.pop() --removes a random value

# ab ham collection mai kuch add karna chahe tooo--
collection=set()
collection.add(1)
collection.add(2)
collection.add(2) # this is repated so it willl be ignored by the set
collection.add(3)
collection.add("apnacollege")

collection.remove(3)
print(collection)

collection.clear()
print(len(collection)) # length should be - 5 , but cleared it so - 0

popcollection={"hello", "apnacollege" ,"world","coding","python"}
print(popcollection.pop())  # any element can be popped in any order

# sets are mutable , but the elements in set are immutable

# SET METHODS
# set.union(set2) -- combines both set values and returns new
# set.intersectionn(set2) -- combines common value & returns new
set1={1,2,3}
set2={2,3,4}
print(set1.union(set2))  #{1,2,3,4}
print(set1.intersection(set2))  #{2,3}