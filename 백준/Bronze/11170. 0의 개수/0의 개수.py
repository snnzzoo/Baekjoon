T = int(input())

for t in range(T):
    N, M = map(int, input().split())
    cnt = 0
    
    for num in range(N, M + 1):
        str_num = str(num)
        cnt += str_num.count('0')
    print(cnt)
        