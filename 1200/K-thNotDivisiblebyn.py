#https://codeforces.com/problemset/problem/1352/C
import sys
import io
 
# Fast I/O using io module (buffered, very fast)d
input = io.TextIOWrapper(sys.stdin.buffer, encoding='utf-8').readline
print = sys.stdout.write
def higher(MID,n,k):
    if MID-MID//n == k:
        return "Found"
    elif MID-MID//n < k:
        return 1
    else:
        return 0
def find_min(M,k,n):
        if M-M//n == k:
            return find_min(M-1,k,n)
        return M+1
for _ in range(int(input())):
    L,U = 0,20**9+1
    n,k = map(int,input().split())
    M = (L+U)//2
    res = higher(M,n,k)
    while res != 'Found':
        res = higher(M,n,k)
        if res == 'Found':
            nth = find_min(M,k,n)
            print(str(nth) +'\n')
            break
        elif res:
            L = M+1
            M = L+(U-L)//2
        else:
             U = M-1
             M = (L+U)//2