t = int(input())
for i in range(t):
    n = input()
    l = int(len(n)/2)
    if n[:l] == n[l:]:
        print('YES')
    else:
        print('NO')
