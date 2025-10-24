# https://codeforces.com/problemset/problem/59/A

n = input()
u = ''
l = ''

for i in n:
    if i.isupper():
        u += i
    else:
        l += i
print(n.upper() if len(u) > len(l) else n.lower())