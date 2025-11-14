# https://codeforces.com/problemset/problem/514/A
invert = {'5':'4','6':'3','7':'2','8':'1','9':'0'}
n = input()
f = ''
flag = True
for i in range(len(n)):
    if n[i] == '9' and i == 0:
        f += n[i]
    elif int(n[i]) > 4:
        f += invert[n[i]]
    else:
        f += n[i]
    flag = False
print(f)