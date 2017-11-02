

def encode(s):
  l = []
  cont = False
  temp_total = 1
  temp_letter = ''
  for i in range(len(s)):
    
    if(i < len(s) - 1 and s[i] == s[i+1]): #If it is the same as the next
      cont = True
    else: #Not same
      cont = False
      
    temp_letter = s[i] #Prepare to add current letter
    
    if(cont == True): # The next letter is the same as this one.
      temp_total += 1

    else: #The next letter is NOT the same; total the letter count, add the letter & reset
      if temp_total > 1:
          l.append(temp_total)
      l.append(temp_letter)
      temp_total = 1
  return l
  
def rle_decode(l):
    str = ""
    num = 1
    for item in l:
        if(type(item) == int):
            num = item
        else:
            str += item * num
            num = 1
    return str
        
    
    
##print('"aaaaab" encodes to', encode("aaaaab"))
##print('"aaaaaaaaaaa" encodes to', encode("aaaaaaaaaaa"))
##print('"bbaaaccaaa" encodes to', encode("bbaaaccaaa"))
##print('"zzzzzyz" encodes to', encode("zzzzzyz"))
##print('"" encodes to', encode(""))
##print('"nothing to see here!" encodes to',encode("nothing to see here!"))

print(rle_decode(encode("aaaaabbbbb")))
print(rle_decode(encode("This has 4 Z's")))
print(rle_decode(encode("Whoooooooooooooooooooooooooooo?")))
print(rle_decode(encode("Nothing here!")))