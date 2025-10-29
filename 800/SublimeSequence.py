# https://codeforces.com/problemset/problem/2148/A
t = int(input())
for _ in range(t):
    n,a = map(int,input().split())
    print(0 if a%2 == 0 else n)