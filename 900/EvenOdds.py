# https://codeforces.com/problemset/problem/318/A
import sys
n,k = map(int,sys.stdin.readline().split())
oddC = (n+1)//2
print(k*2-1 if k <= oddC else 2*(k-oddC))