#next line
str1="this is a string \nwe are creating it in python"
print(str1)

#tab
str2="apna\t college"
print(str2)

#concatenation
str3="latika"
str4="dhami"
print(str3+str4)

#length of str
print(len(str1))
print(len(str4))

final_str = str3+" "+str4
print(final_str)
print(len(final_str))

#agar index 2 wala character chaiye
str="apna college"
#ch=str[2]
#print(ch)
print(str[2])

#slicing ( will be used in ML )
print(str[1:6]) # 1 is included - 6 is not
print(str[7:12]) # 7 is included - 12 th ndex ids not ( there is no 12lth index there is 0 to 11nth index)
print(str[7:len(str)]) # for last y0u say too say len(str) - same as 12
print(str[:4]) # means [0:4]

# negative index in slicing
# that is for APPLE =-5,-4,-3,-2-1
str6="Apple"
print(str6[-3:-1])
