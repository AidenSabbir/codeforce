# https://codeforces.com/problemset/problem/158/A
n = list(map(int,input().split()))

points = list(map(int,input().split()))
nxtlvl = 0
if points[0] >= n[1]:
    for i in range(len(points)-1):
        if points[i] >= points[i+1]:
            nxtlvl += 1
        else:
            pass
    print(nxtlvl-1)
else:
    print(nxtlvl)