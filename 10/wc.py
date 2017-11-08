def remove_non_alpha(w):
    """
    input: w - string representing a "word"
    output: the string with non alpha chars removed
    """
    result=""
    for l in w:
        if l.isalpha():
            result = result + l
    return result

def bwcd(wordlist):
    d={}
    for w in wordlist:
        d.setdefault(w,0)
        d[w] = d[w] + 1
    return d

def bwcff(f):
    """
    input: f - string representing a filename
    returns: a dictionary with keys for words and values
             of the number of times each word occursb
    """
    text = open(f).read()
    l=[]
    for w in text.split():
        w = w.lower()
        w = remove_non_alpha(w)
        l.append(w)
    d = bwcd(l)
    return d


def follow_words(filename):
    text = open(filename).read()
    wordlist = []
    wordgroup = {}
    for word in text.split():
        word = word.lower()
        word = remove_non_alpha(word)
        wordlist.append(word)
        
    for i in range(len(wordlist)):
        wordgroup.setdefault(wordlist[i],[])
        if(i < len(wordlist) - 1):
            wordgroup[wordlist[i]].append(wordlist[i+1])
    return wordgroup
    
    
d = bwcff("hamlet.txt")

print(follow_words("hamlet.txt"))
