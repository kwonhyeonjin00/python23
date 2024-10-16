x1, y1, x2, y2 = map(int, input().split())
a1, b1, a2, b2 = map(int, input().split())

tx = max(x2, a2)
dx = min(x1, a1)

ty = max(y2, b2)
dy = min(y1, b1)

xx = max(tx - dx, ty - dy)

print(xx ** 2)