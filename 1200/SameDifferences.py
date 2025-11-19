# https://codeforces.com/problemset/problem/1520/D
import sys
from collections import Counter
print = sys.stdout.write
for _ in range(int(input())):
    n = int(input())
    arr = list(map(int,input().split()))
    freq = Counter()
    for i in range(n):
        freq[arr[i] - (i+1)] += 1
    c = sum(f * (f - 1) // 2 for f in freq.values())
    print(str(c) + '\n')