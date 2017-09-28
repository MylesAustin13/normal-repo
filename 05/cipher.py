caps_start = ord("A")
lower_start = ord("a")
caps_end = ord("Z")
lower_end = ord("z")
'''
for letter in "abcdefg":
    ascii_val = ord(letter)
    plus = ascii_val + 1
    newchar = chr(plus)
    print(letter,":",ascii_val," rotated: ",newchar,":",plus)
'''
def encode_letter(l,r):
    val = ord(l)
    i = 0
    if(r < 0):
        while (i != r):
        
            if val == lower_start:
                val = lower_end
            elif val == caps_start:
                val = caps_end
            else:
                val -= 1
            i -= 1
    else:
        while (i != r):
        
            if val == lower_end:
                val = lower_start
            elif val == caps_end:
                val = caps_start
            else:
                val += 1
            i += 1
    return chr(val)

def encode_string(s,r):
    result = ""
    for letter in s:
        if (ord(letter) >= caps_start and ord(letter) <= caps_end) or (ord(letter) >= lower_start and ord(letter) <= lower_end):
            result += encode_letter(letter,r)
        else:
            result += letter
            
    return result
def full_encode(s):
    for i in range(26):
        print(encode_string(s,i) + "\n")

print(encode_letter("z",5))
print(encode_string("wxyz",4))
full_encode("Hello, Player 1!")