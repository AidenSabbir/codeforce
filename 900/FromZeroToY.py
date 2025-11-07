# https://codeforces.com/problemset/problem/1488/A
t = int(input())
for _ in range(t):
    x,y = map(int,input().split())
    k = 0
    c = 0
    while k!=y:
        if (x*10)+k <= y:
            k += (x*10)
            c += 1
        elif x+k <= y:
            k += x
            c += 1
        elif k+1 <= y:
            k += 1
            c += 1
    print(c)