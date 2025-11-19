# https://codeforces.com/problemset/problem/474/B
import bisect
import sys
print = sys.stdout.write
input = sys.stdin.readline
m = int(input())
arr = list(map(int,input().split()))
n = int(input())
ju = list(map(int,input().split()))
computearr = []
k = 0
for i in arr:
    k += i
    computearr.append(k)
for i in ju:
    print(str(bisect.bisect_left(computearr,i)+1)+'\n')
    