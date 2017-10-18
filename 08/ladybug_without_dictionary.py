#!/bin/python3

import sys
n = 0
b = ''



    
def isHappy():
        
    happybugs = []
    for bug in b:
        happybugs.append(0) #0 = unhappy, 1 = happy
    for i in range(len(b)):
        if i == 0: #First bug
            if b[i+1] == b[i]:
                happybugs[i] = 1
                
        if i == len(b) - 1: #Last bug
            if b[i-1] == b[i]:
                happybugs[i] = 1
        
        else: #in the middle
            if b[i+1] == b[i] or b[i-1] == b[i]:
                happybugs[i] = 1
    
    if 0 in happybugs:
        return False
    else:
        return True

def isLonely(counts,colorings):
    for i in range(len(counts)):
        if(colorings[i] != '_'):
            if(counts[i] == 1):
                return True
    return False
    

def getColors():
    colors = []
    for bug in b:
        if(bug not in colors):
            colors.append(bug)
    nums = []
    for item in colors:
        nums.append(0)
  #  print(nums)
    for bug in b:
        if(bug in colors):
          #  print(bug)
          #  print(colors.index(bug))
            nums[colors.index(bug)] += 1
    currentlyHappy = isHappy()
    if('_' not in colors and not currentlyHappy): #No room, not solved
        return False
    if(isLonely(nums,colors)):#Lonely bug
        return False
    return True

Q = int(input().strip())
for a0 in range(Q):
    n = int(input().strip())
    b = input().strip()
    if getColors() == True:
        print("YES")
    else:
        print("NO")


    