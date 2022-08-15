N = int(input()) # 손님 수
seats = list(map(int, input().split())) # 원하는 자리

# 중복되는 자리 번호 제거하고 리스트 길이(거절당하지 않은 사람 수)
s = len(set(seats))

# 손님 수에서 거절당하지 않은 사람 빼기
print(N - s)
