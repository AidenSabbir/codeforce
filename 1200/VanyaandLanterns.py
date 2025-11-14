# https://codeforces.com/problemset/problem/492/B
n,l = map(int,input().split())
arr = list(set(map(int,input().split())))
arr.sort()
maxi = float('-inf')
for i in range(len(arr)-1):
    if arr[i+1] - arr[i] > maxi:
        maxi = arr[i+1] - arr[i]
print(f"{max(maxi/2,arr[0]-0,l-arr[-1]):.10f}")