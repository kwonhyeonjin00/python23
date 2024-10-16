n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

min_x = arr[0][0]
max_x = arr[0][1]
min_idx = 0
max_idx = 0
for i in range(n):
    if arr[i][0] < min_x:
        min_idx = i
        min_x = arr[i][0]
    if arr[i][1] > max_x:
        max_idx = i
        max_x = arr[i][1]

a = arr[min_idx][1] - arr[min_idx][0]
b = arr[max_idx][1] - arr[max_idx][0]

if a >= b:
    arr.pop(min_idx)
else:
    arr.pop(max_idx)

min_x = arr[0][0]
max_x = arr[0][1]

for i in range(n - 1):
    if arr[i][0] < min_x:
        min_x = arr[i][0]
    if arr[i][1] > max_x:
        max_x = arr[i][1]

print(max_x - min_x)