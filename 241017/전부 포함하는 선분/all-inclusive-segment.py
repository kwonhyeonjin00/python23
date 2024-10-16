n = int(input())
arr = [list(map(int, input().split())) for _ in range(n)]

ans = 101

for i in range(n):
    a = 101
    b = 0
    for j in range(n):
        if i == j:
            continue
        if arr[j][0] < a:
            a = arr[j][0]
        if arr[j][1] > b:
            b = arr[j][1]

    ans = min(ans, b - a)

print(ans)