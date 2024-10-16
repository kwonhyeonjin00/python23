n = int(input())
arr = list(map(int, input().split()))

cnt = 0

x = arr.pop()
chk = 0

for i in range(n - 1):
    t = arr.pop()
    if t + 1 == x:
        chk += 1
        x = t
    else:
        print(n - chk)
        break