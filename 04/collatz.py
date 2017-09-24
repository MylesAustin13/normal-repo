def collatz(num):
    if(num % 2 == 0):
        num = num // 2
        print(num)
        return num
    else:
        num = 3 * num + 1
        print(num)
        return num
    
while True:
    start = input("Enter an integer.")
    try:
        start = int(start)
    except:
        print("Please give a valid number.")
        continue
    break

while start != 1:
    start = collatz(start)