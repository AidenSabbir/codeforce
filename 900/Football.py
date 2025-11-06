#https://codeforces.com/problemset/problem/96/A
import sys
read = sys.stdin.readline
write = sys.stdout.write

n = read().strip()
count = 1
for i in range(1, len(n)):
    if n[i] == n[i-1]:
        count += 1
        if count == 7:
            write('YES')
            break
    else:
        count = 1
else:
    write('NO')
