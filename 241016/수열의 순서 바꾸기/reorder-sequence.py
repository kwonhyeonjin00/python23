n = int(input())
arr = list(map(int, input().split()))

cnt = 0

x = arr.pop()
chk = 1
t = 0
for i in range(n - 1):
    #print(arr[n - 2 - i])
    if arr[n - 2 - i] + 1 < x:
        chk += 1
        x = arr[n - 2 - i]
    else:
        print(n - chk)
        t = 1
        break

if t == 0:
    print(0)