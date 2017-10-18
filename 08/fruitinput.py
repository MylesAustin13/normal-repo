#!/bin/python3

import sys


s,t = input().strip().split(' ')
s,t = [int(s),int(t)]
a,b = input().strip().split(' ')
a,b = [int(a),int(b)]
m,n = input().strip().split(' ')
m,n = [int(m),int(n)]
apple = [int(apple_temp) for apple_temp in input().strip().split(' ')]
orange = [int(orange_temp) for orange_temp in input().strip().split(' ')]


def applefinder(housestart,houseend):
    total = 0
    for fr in apple:
        if fr + a >= housestart and fr + a <= houseend:
            total += 1
    return total

def orangefinder(housestart,houseend):
    total = 0
    for fr in orange:
        if fr + b >= housestart and fr + b <= houseend:
            total += 1
    return total

print(applefinder(s,t))
print(orangefinder(s,t))