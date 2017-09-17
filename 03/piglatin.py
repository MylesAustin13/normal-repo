def piglatinify(str):
    format = ""
    if(str[0] == "a" or str[0] == "e" or str[0] == "i" or str[0] == "o" or str[0] == "u"):
        format = str + "ay"
    else:
        format = str[1:] + str[0] + "ay"
    return format

testA = piglatinify("thumb")
print(testA)
testB = piglatinify("apple")
print(testB)
testC = piglatinify("kitten")
print(testC)