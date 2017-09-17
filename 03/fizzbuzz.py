def fizzbuzz(min,max):
    line = ""
    print("----------------------")
    flaghit = False
    while min <= max:
    #for min in range(max):
        if min % 3 == 0:
            line += "fizz"
            flaghit = True
        if min % 5 == 0:
            line += "buzz"
            flaghit = True
        if(flaghit):
            print(line)
        else:
            print(min)
        line = ""
        flaghit = False
        min+=1
        
fizzbuzz(0,101)