# https://codeforces.com/problemset/problem/489/B
import sys
print = sys.stdout.write
input = sys.stdin.readline
nb = int(input())
barr = list(map(int,input().split()))
barr.sort()
ng = int(input())
garr = list(map(int,input().split()))
garr.sort()
pairs = 0
L = 0
R = 0
while R < nb and L < ng:
    if (max(barr[R],garr[L])-min(barr[R],garr[L]))//2 == 0:
        pairs += 1
        R += 1
        L += 1
    else:
        if barr[R] < garr[L]:
            R += 1
        else:
            L += 1
print(str(pairs) + '/n')
