import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    x1, y1, r1, x2, y2, r2 = map(int, input().split())

    dx = x1 - x2
    dy = y1 - y2
    d2 = dx*dx + dy*dy

    if d2 == 0:
        print(-1 if r1 == r2 else 0)
        continue

    sum_r2 = (r1 + r2) ** 2
    diff_r2 = (r1 - r2) ** 2

    if d2 > sum_r2 or d2 < diff_r2:
        print(0)
    elif d2 == sum_r2 or d2 == diff_r2:
        print(1)
    else:
        print(2)