# https://codeforces.com/problemset/problem/158/A
n, k = map(int,input().split())
scores = list(map(int,input().split()))
kthScore = scores[k-1]
count = 0
if sum(scores) != 0:
    for i in scores:
        if i >= kthScore and i > 0:
            count += 1
    print(count)
else:
    print(count)