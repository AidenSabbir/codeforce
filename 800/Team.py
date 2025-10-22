#https://codeforces.com/problemset/problem/231/A
n = int(input())
count = 0
for i in range(n):
    views = list(map(int,input().split()))
    if sum(views) >= 2:
        count += 1
print(count)