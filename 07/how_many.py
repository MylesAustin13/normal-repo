def freq(sought_int, list):
    occurences = 0
    for int in list:
        if int == sought_int:
            occurences += 1
    return occurences
    
def min(list):
    min = list[0]
    for i in list:
        if (list[i] < min):
            min = list[i]
    return min

def mode(list):
    result = 0
    result_occur = 0
    for int in list:
        if freq(int,list) > result_occur:
            result = int
            result_occur = freq(int,list)
    return result


print(freq(3,[3,4,5,5,3,2,3,3]))
print(min([1,2,3,4,5,6,8,9,5,3,4]))
print(mode([3,4,5,5,3,2,3,3]))