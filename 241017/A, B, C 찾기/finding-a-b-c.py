arr = list(map(int, input().split()))

A = arr.pop(arr.index(min(arr)))

B = min(arr)

ABC = max(arr)
C = ABC - (A + B)

print(A, B, C)