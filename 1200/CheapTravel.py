# https://codeforces.com/problemset/problem/466/A
import math
arr = list(map(int,input().split()))
ride = arr[0]
multi = arr[1] 
single_c = arr[2]
multi_c = arr[3]
cost = 0
while ride > 0:
    if (math.ceil(ride/multi)*multi_c) < ride*single_c:
        ride -= multi
        cost += multi_c
    else:
        ride -= 1
        cost += single_c
print(int(cost))



        