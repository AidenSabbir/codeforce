#https://codeforces.com/problemset/problem/112/A
n = input().lower()
m = input().lower()

if n < m:
    print(-1)
if n > m:
    print(1)
if n == m:
    print(0)