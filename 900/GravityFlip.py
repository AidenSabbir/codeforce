# https://codeforces.com/problemset/problem/405/A
import sys
n = int(sys.stdin.readline())
arr = list(map(int, sys.stdin.readline().split()))
sys.stdout.write(' '.join(map(str, sorted(arr))))
