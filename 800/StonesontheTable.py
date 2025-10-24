n = int(input())
s = input()
c = 0
for r in range(1,n):
    if s[r] == s[r-1]:
        c += 1
print(c)