# https://codeforces.com/problemset/problem/750/A
import io,os,sys
input = io.BytesIO(os.read(0,os.fstat(0).st_size)).readline
print = sys.stdout.write
c = 0
n,k = map(int,input().split())
time = 240
for i in range(1,n+1):
    time -= 5*i
    if time >= k:
        c += 1
print(str(c))