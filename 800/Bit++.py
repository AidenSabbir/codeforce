#https://codeforces.com/problemset/problem/282/A
from collections import Counter
n = int(input())
count = 0
for _ in range(n):
    x = input().lower().strip('x')
    if x == '++':
        count += 1
    elif x == '--':
        count -= 1
print(count)