import math

english_vector = [8.12,1.49,2.71,4.32,12.02,2.30,2.03,5.92,7.31,.10,.69,3.98,2.61,6.95,7.68,1.82,.11,6.02,6.28,9.10,2.88,1.11,2.09,.17,2.11,.07]

#for testing purposes 
alph = "abcdefghijklmnopqrstuvwxyz"
alph_list = alph.split()

caps_start = ord("A")
lower_start = ord("a")
caps_end = ord("Z")
lower_end = ord("z")

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
    rotations = []
    for i in range(26):
        rotations.append(encode_string(s,i))
    return rotations

def countLetter(letter,sentence):
    count = 0
    for l in sentence:
        if letter == l:
            count += 1
    return count

def getVector(str):
    sentence_vector = []
    str = str.lower()
    letter_total = 0
    for letter in str:
        if letter in "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ":
            letter_total += 1
    #print(letter_total)
    i = ord('a')
    while i <= ord ('z'):
        sentence_vector.append((countLetter(chr(i),str) / letter_total) * 100)
        i += 1
    return sentence_vector

def distancer(vect):
    to_root = 0
    i = 0
    while i < len(vect):
        to_root += (vect[i] - english_vector[i]) * (vect[i] - english_vector[i])
        i += 1
    return math.sqrt(to_root)

def decode(str):
    rotations = full_encode(str)
    #print(rotations)
    selected_index = -1
    min = math.inf
    i = 0
    while i < len(rotations):
        temp = distancer(getVector(rotations[i]))
        if temp < min:
            min = temp
            selected_index = i
        i += 1
    return rotations[selected_index]


string = "Hello! This sentence is designed to test the functionality of these routines!"
string = encode_string(string, 5)
print("Given: ",string)
print("Decoded: ",decode(string))