# https://codeforces.com/problemset/problem/327/A
n = int(input())
arr = list(map(int,input().split()))
L,R = 0,n-1
total = 0
while L < R:
    value = arr[L:R+1].count(0) - arr[L:R+1].count(1)
    total = max(total,value)
    if arr[R] == 0 and arr[L] == 0:
        L += 1
        R -= 1
    while arr[L] != 0:
        L += 1
    while arr[R] != 0:
        R -= 1
if n == 1 and arr[0] == 1:
    print(0)
elif n == 1 and arr[0] == 0:
    print(1)
else:
    print(arr.count(1)+total)