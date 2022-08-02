T = int(input())

for t in range(T):
    r, e, c = list(map(int, input().split()))
    if r > e - c:
        print('do not advertise')
    elif r < e - c:
        print('advertise')
    else:
        print('does not matter')