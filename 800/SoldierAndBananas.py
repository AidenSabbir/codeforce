#https://codeforces.com/problemset/problem/546/A

k,n,w = list(map(int,input().split()))
total = 0
for i in range(w+1):
    total += k*i
print(0 if total-n <0 else total-n)
