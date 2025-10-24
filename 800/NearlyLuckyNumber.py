# https://codeforces.com/problemset/problem/110/A
n = input()
r = 0
for i in n:
    if i not in ('4','7'):
        r += 1
print('NO' if r else 'YES')