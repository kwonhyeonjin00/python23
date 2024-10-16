n = int(input())
arr = list(map(int, input().split()))
arr.sort()

ans = 10000000000

for i in range(n):
    t = arr[i+n] - arr[i]
    ans = min(ans, t)

print(ans)