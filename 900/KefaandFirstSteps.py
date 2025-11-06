# https://codeforces.com/problemset/problem/580/A
import sys
n = int(sys.stdin.readline())
arr = list(map(int,sys.stdin.readline().split()))
c = 1
maxl = 1
for i in range(n-1):
    if arr[i] <= arr[i+1]:
        c += 1
    if arr[i] > arr[i+1]:
        c = 1
    maxl = max(maxl,c)
sys.stdout.write(str(maxl))