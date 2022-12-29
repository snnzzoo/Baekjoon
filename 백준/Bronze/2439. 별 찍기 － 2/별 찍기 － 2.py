N = int(input())
cnt = 0

for n in range(1, N + 1):
    cnt += 1
    print(((N - cnt) * " ") + ("*" * cnt))
