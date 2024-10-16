def check(arr):
    for i in range(n):
        if arr[i] != i - 1:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))

chk_num = max(arr)

cnt = 0
x = 0

while True:
    c = 0
    t = []
    if check(arr):
        print(cnt)
        break

    while True:
        if c == 1:
            break 

        if arr[0] == x + 1:
            t.append(arr.pop(0))
            x = t[-1]
        else:
            c = 1

    if t[-1] == chk_num:
        cnt += len(t)
        for i in range(len(t)):
            arr.append(t.pop(0))

    else:
        cnt += len(t)
        idx = arr.index(min(arr))

        for i in range(len(t)):
            arr.insert(idx, t.pop())
    print(arr)

print(cnt)