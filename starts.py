n = int(input(": "))
for i in range(n):
    for j in range((n-i)):
        print(' ',end='')
    if i <= 4 or n-i <= 2:
        print("* "*i)
    else:
        print(f'* * {"  "*(i-4)}* *')