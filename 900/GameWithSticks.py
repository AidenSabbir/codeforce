# https://codeforces.com/problemset/problem/451/A
import sys
input = sys.stdin.readline
print = sys.stdout.write
n,m = map(int,input().split())
mini = min(n,m)
if mini%2 == 0:
    print('Malvika\n')
else:
    print('Akshat\n')