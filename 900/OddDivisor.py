# https://codeforces.com/problemset/problem/1475/A
import sys
input = sys.stdin.readline
print = sys.stdout.write
T = int(input())
for _ in range(T):
    n = int(input())
    Flag = True
    if n%2 == 0:
        while Flag:
            d = n//2
            if n == 2:
                print('NO\n')
                Flag = False
            if d%2 != 0 and d != 1:
                print('YES\n')
                Flag = False
            n = d
    else:
         print('YES\n')