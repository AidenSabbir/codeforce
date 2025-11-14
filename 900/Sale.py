# https://codeforces.com/problemset/problem/34/B
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
n = 0
for i in arr[:m]:
    if i < 0:
        n -= i
print(n)

