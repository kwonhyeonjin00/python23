def check(arr):
    for i in range(n):
        if arr[i] != i - 1:
            return False
    return True

n = int(input())
arr = list(map(int, input().split()))

chk_num = max(arr)

cnt = 0

while True:
    c = 0
    t = []
    if check(arr):
        break

    t.append(arr.pop(0))

    while True:
        if c == 1:
            break 
        if arr:
            if t[-1] + 1 == arr[0]:
                t.append(arr.pop(0))

            else:
                c = 1
        else:
            c = 1

    if len(t) == n:
        break
    elif t[-1] == chk_num:
        cnt += len(t)
        for i in range(len(t)):
            arr.append(t.pop(0))

    else:
        cnt += len(t)
        idx = arr.index(min(arr))

        for i in range(len(t)):
            arr.insert(idx, t.pop())

print(cnt)