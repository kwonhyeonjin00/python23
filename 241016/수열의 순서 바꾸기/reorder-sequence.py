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
    if check(arr):
        print(cnt)
        break

    t = arr.pop(0)
    if t == chk_num:
        print(cnt + 1)
        break

    idx = arr.index(min(arr))

    arr.insert(idx, t)
    cnt += 1