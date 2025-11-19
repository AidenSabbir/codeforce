# https://codeforces.com/problemset/problem/433/B
import sys
print = sys.stdout.write
def pre_compute(arr):
    n = len(arr)
    total = 0
    pre = [0]*(n+1)
    for i in range(n):
        total += arr[i]
        pre[i+1] = total
    return pre

n  = int(input())
arr = list(map(int,input().split()))
pre = pre_compute(arr)
sor = pre_compute(sorted(arr))
q = int(input())
for _ in range(q):
    type,l,r  = map(int,input().split())
    if type == 1:
        print(str(pre[r]-pre[l-1]) + '\n')
    else:
        print(str(sor[r]-sor[l-1]) + '\n')
