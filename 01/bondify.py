str = "Sheldon Dinkleberg"
spaceindex = str.find(" ",0)
lastname = str[spaceindex:]
format = lastname + ", " + str + "."
print(format)
