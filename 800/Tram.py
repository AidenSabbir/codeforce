# https://codeforces.com/problemset/problem/116/A
t = int(input())
H = 0
current = 0
for _ in range(t):
    n,m = map(int,input().split())
    current -= n
    current += m
    if H <= current:
        H = current
print(H)
