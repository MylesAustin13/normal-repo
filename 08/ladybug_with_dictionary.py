import sys
    
def isHappy(bugstring):
        
    happybugs = []
    for bug in bugstring:
        happybugs.append(0) #0 = unhappy, 1 = happy
    for i in range(len(bugstring)):
        if i == 0: #First bug
            if bugstring[i+1] == bugstring[i]:
                happybugs[i] = 1
                
        if i == len(bugstring) - 1: #Last bug
            if bugstring[i-1] == bugstring[i]:
                happybugs[i] = 1
        
        else: #in the middle
            if bugstring[i+1] == bugstring[i] or bugstring[i-1] == bugstring[i]:
                happybugs[i] = 1
    
    if 0 in happybugs:
        return False
    else:
        return True
    
    
def isLonely(bug_dict):
    for each in bug_dict.keys():
        if(each != "_" and bug_dict[each] == 1):
            #print(each)
            return True
    return False    

def getColors(bugstring):
    ladybugs = {}
    
    for bug in bugstring:
        if(bug in ladybugs.keys()):
            ladybugs[bug] += 1
        else: 
            ladybugs.setdefault(bug,1)
            
            
    currentlyHappy = isHappy(bugstring)
    if('_' not in ladybugs.keys() and not currentlyHappy): #No room, not solved
        return False
    if(isLonely(ladybugs)):#Lonely bug
        return False
    return True

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    if getColors(b) == True:
        print("YES")
    else:
        print("NO")

