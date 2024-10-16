arr = list(map(int, input().split()))

A = arr.pop(arr.index(min(arr)))

B = arr.pop(arr.index(min(arr)))

C = arr.pop(arr.index(min(arr)))

ABCD = max(arr)
D = ABCD - (A + B + C)

print(A, B, C, D)