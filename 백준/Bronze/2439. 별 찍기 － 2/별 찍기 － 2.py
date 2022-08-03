N = int(input())
star = 0
blank = N

for n in range(N):
    star += 1
    blank -= 1
    print(' ' * blank + '*' * star)