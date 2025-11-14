# https://codeforces.com/problemset/problem/1374/B
T = int(input())
for _ in range(T):
    n = int(input())
    c = 0
    while n != 1:
        if n%6 == 0:
            n = n//6
            c += 1
        else:
            if (n*2)%6 ==0:
                n *= 2
                c += 1
            else:
                break
    print(c if n == 1 else -1)
