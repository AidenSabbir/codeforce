#https://codeforces.com/problemset/problem/263/A

r = c = 0
for _ in range(1,6):
    n = list(map(int,input().split()))
    for i,v in enumerate(n,start=1):
        if v == 1:
            r,c = i,_
print(abs(r-3) + abs(c-3))