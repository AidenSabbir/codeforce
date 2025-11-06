# https://codeforces.com/problemset/problem/160/A
import sys
n = int(sys.stdin.readline())
coins = list(map(int, sys.stdin.readline().split()))
coins.sort(reverse=True)
total = sum(coins)
curr = 0
count = 0

for coin in coins:
    curr += coin
    count += 1
    if curr > total - curr:  
        break
sys.stdout.write(str(count))
