# https://codeforces.com/problemset/problem/750/A
import sys
c = 0
n,k = map(int,input().split())
time = 240
for i in range(1,n+1):
    time -= 5*i
    if time >= k:
        c += 1
sys.stdout.write(str(c))