T = int(input())
cost = 0

for t in range(T):
    s = int(input()) # 자동차 가격
    n = int(input()) # 옵션 개수
    cost = s
    
    for i in range(n):
        q, p = map(int, input().split()) # 옵션 개수, 옵션 가격
        # print(q, p)
        cost += (q * p)

    print(cost)