# https://codeforces.com/problemset/problem/677/A
n , h = map(int,input().split())
fh = list(map(int,input().split()))
print(sum(1 if i <= h else 2 for i in fh))
