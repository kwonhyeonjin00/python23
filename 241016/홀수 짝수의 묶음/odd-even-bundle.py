n = int(input())
arr = list(map(int, input().split()))

even, odd = 0, 0
for i in arr:
    if i % 2 == 0:
        even += 1
    elif i % 2 == 1:
        odd += 1

if even > odd:
    print(odd * 2 + 1)

elif even == odd:
    print(odd * 2)

elif even < odd:
    cnt = 0
    cnt += even
    odd -= even

    k = 2

    while True:
        if odd <= 0:
            break

        elif odd == 2 and k == 1:
            break

        if odd >= 2 and k == 2:
            odd -= k
            cnt += 1
            k = 1

        elif odd > 1 and k == 1:
            odd -= k
            cnt += 1
            k = 2

        elif odd == 1 and k == 1:
            odd -= k
            cnt += 1

print(cnt)