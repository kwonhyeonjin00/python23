n = int(input())

arr = [list(map(int, input().split())) for _ in range(n)]

arr.sort()

a = arr[0][1] - arr[0][0]
b = arr[n - 1][1] - arr[n - 1][0]

if a >= b:
    print(arr[n - 1][1] - arr[1][0])

else:
    print(arr[-2][1] - arr[0][0])