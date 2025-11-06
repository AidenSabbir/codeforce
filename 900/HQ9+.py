# https://codeforces.com/problemset/problem/133/A
import sys

n = set(sys.stdin.readline().strip())
sys.stdout.write('YES' if n & {'H','Q','9'} else 'NO')

    