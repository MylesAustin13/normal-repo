def string_times(str, n):
  format = str * n
  return format

def front_times(str, n):
  if(len( str ) < 3):
    format = str * n
  else:
    format = str[0:3] * n
  return format

def string_bits(str):
  i = 0
  format = ""
  while(i < len (str)):
    format += str[i]
    i+=2
  return format

def lone_sum(a, b, c):
  sum = 0
  if(a != b and a != c):
    sum += a
  if(b != a and b != c):
    sum += b
  if(c != a and c != b):
    sum += c
    
  return sum
    
def string_splosion(str):
  i = 0
  format = ""
  while(i <= len(str)):
    format += str[0:i]
    i += 1
  return format

def cigar_party(cigars, is_weekend):
  if(is_weekend == False):
    if(cigars > 60 or cigars < 40):
      return False
  else:
    if(cigars < 40):
      return False
  return True

def caught_speeding(speed, is_birthday):
  upperthreshold = 80
  lowerthreshold = 60
  if(is_birthday):
    upperthreshold += 5
    lowerthreshold += 5
  if(speed <= lowerthreshold):
    return 0
  elif(speed > lowerthreshold and speed <= upperthreshold):
    return 1
  elif(speed > upperthreshold):
    return 2

print(string_times("hi",5))
print(front_times("Howdy",4))
print(string_bits("powerful"))
print(lone_sum(1,1,8))
print(string_splosion("ghost"))
print(cigar_party(50,False))
print(caught_speeding(73,True))