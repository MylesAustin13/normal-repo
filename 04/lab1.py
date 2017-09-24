#Yan, Leman & Austin, Myles
import random

story = '''
There once was a NOUN that VERB. The ADJECTIVE NOUN  VERB. Then the NOUN VERB. 
'''

nouns = ['boy','person','kitten','ghost','pepper']
verbs = ['walked','flew','ate','fell','exploded']
adjective=['cool','nice','angry','sad','salty']
hasperiod = False
words=story.split()

def function(story):
    i=0
    result = ""
    while i<len(words):
        if '.' in words[i]:
            hasperiod = True
        else:
            hasperiod = False

        if 'NOUN' in words[i]:
            picknoun(i)
        elif 'VERB' in words[i]:
            pickverb(i)
        elif 'ADJECTIVE' in words[i]:
            pickadj(i)
        
        if hasperiod == True:
            words[i] = insertperiod(words[i])
        i=i+1
    for x in words:
        result += x + " "
    print(result)
        
def picknoun(index):
    rdm=random.randrange(0,len(nouns))
    words[index]=nouns[rdm]

def pickverb(index):
    rdm=random.randrange(0,len(verbs))
    words[index]=verbs[rdm]
    
def pickadj(index):
    rdm=random.randrange(0,len(adjective))
    words[index]=adjective[rdm]
    
def insertperiod(str):
    str += "."
    return str
    
function(story)

    