# https://codeforces.com/problemset/problem/734/A
n = input()
s = list(input().lower())
print('Anton' if s.count('a') > s.count('d') else ('Danik' if s.count('d') > s.count('a') else 'Friendship') )