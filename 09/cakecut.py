
def divide(A,B,u):
  if(A == 0): #If ratio = 0, prevent error
    return 0
  ratio = A / B #get the ratio
  people = u / ratio #See how many of the given ratio fits into the number of cakes
  return int(people) #return the integer
  
print("If each were to get 5 / 10 units of cake, and there is 1 cake, he should invite ",divide(5,10,1),"people.")
print("If each were to get 5 / 4 units of cake, and there are 20 cakes, he should invite ",divide(5,4,20),"people.")
print("If each were to get 5 / 10 units of cake, and there are 3.5 cakes, he should invite ",divide(5,10,3.5),"people.")
print("If each were to get 1 / 13 units of cake, and there are 2 cakes, he should invite ",divide(1,13,2),"people.")
print("If each were to get 0 / 1 units of cake, and there is 1 cake, he should invite ",divide(0,1,1),"people.")
print("If each were to get 3 / 4 units of cake, and there is 1 cake, he should invite ",divide(3,4,1),"people.")
print("If each were to get 1 / 2 units of cake, and there no cake, he should invite ",divide(1,2,0),"people.")

