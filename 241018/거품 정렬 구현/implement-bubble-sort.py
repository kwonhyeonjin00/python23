n = int(input())
arr = list(map(int, input().split()))

for i in range(n - 1):
    for j in range(n - 1):
        if arr[j] > arr[j + 1]:
            arr[j], arr[j + 1] = arr[j + 1], arr[j]

for x in arr:
    print(x, end=' ')