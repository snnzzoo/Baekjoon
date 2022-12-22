h, m = map(int, input().split())

if 45 <= m <= 59:
    print(h, m - 45)
elif 0 < h:
    print(h - 1, m + 15)
else:
    print(23, m + 15)
