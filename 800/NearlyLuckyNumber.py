# https://codeforces.com/problemset/problem/110/A
n = list(map(int,input()))
c = sum(1 for d in n if d in (4,7))
print("YES" if c in (4,7) else 'NO')