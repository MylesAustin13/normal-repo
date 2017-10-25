def score(w):
  points = {1:'AEIOULNRST', 2:'DG', 3:'BCMP', 4:'FHVWY', 5:'K', 8:'JX', 10:'QZ'}
  total = 0
  w = w.upper()
  for char in w:
    
    for v in points.keys():

      if char in points[v]:
        total += v
        #print(total)
  return total

print("'hello' is worth", score("hello"), "points.")
print("'ghoulish' is worth", score("ghoulish"), "points.")
print("'weird' is worth", score("weird"), "points.")
print("'' is worth", score(""), "points.")