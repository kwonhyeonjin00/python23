n = int(input())
arr0 = []
arr1 = []

for i in range(n):
    a, b = map(int, input().split())
    arr0.append(a)
    arr1.append(b)

max_x1 = arr1.pop(arr1.index(max(arr1)))
max_x2 = arr1.pop(arr1.index(max(arr1)))

min_x1 = arr0.pop(arr0.index(min(arr0)))
min_x2 = arr0.pop(arr0.index(min(arr0)))

if max_x1 - max_x2 >= min_x2 - min_x1:
    print(max_x2 - min_x1)
else:
    print(max_x1 - min_x2)