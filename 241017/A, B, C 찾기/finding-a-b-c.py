arr = list(map(int, input().split()))

A = arr.pop(arr.index(min(arr)))

ABC = arr.pop(arr.index(max(arr)))

BC = ABC - A

for i in range(len(arr) - 1):
    for j in range(i + 1, len(arr)):
        if arr[i] + arr[j] == BC:
            if arr[i] <= arr[j]:
                B = arr[i]
                C = arr[j]
            else:
                B = arr[j]
                C = arr[i]

print(A, B, C)