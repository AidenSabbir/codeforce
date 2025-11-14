# https://codeforces.com/problemset/problem/313/A
n = input()
if int(n) >= 0 or len(n) == 2:
    print(int(n))
else:
    if n[-1] > n[-2]:
        print(n[:-1])
    else:
        print(int(n[:-2]+n[-1]))