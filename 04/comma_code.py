def comma(givenlist):
    max = len(givenlist) - 1
    bigstring = ""
    i = 0
    while (i <= max):
        if(i == max):
            bigstring += "and " + givenlist[i]
        elif(i < max):
            bigstring += givenlist[i] + ", "
        i+=1
    return bigstring

test = ["butter","milk","eggs","apples","grapes"]
print(comma(test))