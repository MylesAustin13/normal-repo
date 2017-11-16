import csv

def remove_non_alpha(w):
    """
    input: w - string representing a "word"
    output: the string with non alpha chars removed
    """
    result=""
    for l in w:
        if l.isalpha() or l == " ":
            result = result + l
    return result

def read_it(has_key,key_index,filename):
    f = open(filename)
    print("Building dictionary...")
    csv_reader = csv.reader(f)
    l = [] #List containing every entry
    dict = {} #Dictionary to be returned
    for line in csv_reader:
        l.append(line)
    
    if(has_key == True):
        #if the file has a key, drop the first line.
        l.pop(0)
    
    scrambled_words = []
    unique_words = []
    for each_line in l:
        for each_item in each_line:
            each_item = each_item.split(' ')
            if len(each_item) == 1:
                scrambled_words.append(each_item)
            elif len(each_item) > 1:
                
                for term in each_item:
                    scrambled_words.append(term)
            else:
                continue
    
    for i in range(len(scrambled_words)):
        #print(len(scrambled_words))
        #print(scrambled_words[44491])
        scrambled_words[i] = ''.join(scrambled_words[i])
        scrambled_words[i] = scrambled_words[i].lower()
        scrambled_words[i] = remove_non_alpha(scrambled_words[i])
    
    for word in scrambled_words:
        if(word != ""):
            dict.setdefault(word,[])
    print("Finding word occurrences...")
    count = 0
    #print(l)
    for each_key in dict:
        for each_line in l:
            #print(each_key, remove_non_alpha(" ".join(each_line).lower()))
            
            if each_key in remove_non_alpha(" ".join(each_line).lower()):
                count += 1
                dict[each_key].append(each_line[key_index])
##    striplist = []
##    for group in l:
##        striplist.append(group[:key_index] + group[key_index+1:])
##

##    for eachline in striplist:
##        for item in eachline:
##            temp = str(item)
##            temp = temp.split()
##            for word in temp:
##                word = word.lower()
##                word = remove_non_alpha(word)
##                dict.setdefault(word,[])
##    print("Halfway There!")
##    for k in dict.keys():
##
##        print(k, line)
##        if any(k in remove_non_alpha(s.lower()) for s in line for line in l):
##            print(line[key_index])
##            dict[k].append(line[key_index])
##
##    
    f.close()
    print("Dictionary complete!")
    return dict
##    print(len(dict))
##    print(count)
    #return dict



#read_it(True,2,"sample.csv")
test = read_it(True,3,"offenders-clean.csv")

print("occurrence of 'mikel': ",test['mikel'])
print("occurrence of 'sorry': ",test['sorry'])
print("occurrence of 'god': ",test['god'])