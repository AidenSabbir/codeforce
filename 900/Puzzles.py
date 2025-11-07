# https://codeforces.com/problemset/problem/337/A
n,m = map(int,input().split())
arr = list(map(int,input().split()))
arr.sort()
mini = float('inf')
for i in range(m-n+1):
    diff = arr[n+i-1] - arr[i]
    if diff < mini:
        mini = diff
print(mini)

