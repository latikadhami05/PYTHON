# TUPLES in python
#  a built-in data type that lets us create immutable sequences of values

# tuple mai curve bracket () list mai []

tup=(2,1,3,1)
print(tup[0])
print(tup[1])
# tup[0]=5 # this is not allowed in python because its immutable , cannot be changed- cnats assign items

tup=()
print(tup)
print(type(tup))

# cant write tup(1) but tup(1,) kyuki tup(1) mai python use integer samjhega value mai 1 print hoga aur type integer prnt ho jayega , soo for perceive it as a tuple u must (1,)
tup=(1,)
print (tup)
print(type(tup))

# TUPLE METHODS
# tup.index(el) -- returns index of first occurrence , tup.index(1) is 1
# tup.count(el) --counts total occurences , tup.count(1) is 2
tup=(1,2,3,3,3,4)
print(tup.index(4))
print(tup.count(3))


