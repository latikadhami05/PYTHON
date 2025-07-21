#STRING FUNCTIONS
str="i am a coder from studing python from apna college"

print(str.endswith("ege") )#returns true if string ends with substring( last of that string-line mai (ege) hai ki nahi - jo ki hai ( true))
print(str.capitalize() )#capitalizes 1st char

print(str.replace("o","a")) #replaces all occurences of old with new - ( "old","new")
print(str.replace("python","javascript"))

print(str.find("o")) #returns 1st index of 1st occurrer
print(str.find("coder"))
print(str.find("Q")) # jo chiz dont exist the answer ill get is -1

print(str.count("from")) #counts the occurence of substring

