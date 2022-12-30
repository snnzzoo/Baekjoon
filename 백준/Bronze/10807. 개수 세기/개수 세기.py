N = int(input())
list = list(map(int, input().split()))
v = int(input())
cnt = 0

for n in range(N):
    if v == list[n]:
        cnt += 1
print(cnt)