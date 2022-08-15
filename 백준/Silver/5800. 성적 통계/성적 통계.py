K = int(input()) # 반의 수

for k in range(1, K + 1):
    score = list(map(int, input().split()))
    score = score[1:] 
    sorted_score = sorted(score) # 최대, 최소, gap 구하기 위해 score 리스트 오름차순 정렬
    # print(sorted_score)

    max_score = sorted_score[-1]
    min_score = sorted_score[0]
    gap_list = [] # 최대 차이를 구하기 위해 gap 빈 리스트

    for i in range(len(sorted_score) - 1):
        gap = sorted_score[i + 1] - sorted_score[i]
        gap_list.append(gap)

    print(f'Class {k}')
    print(f'Max {max_score}, Min {min_score}, Largest gap {max(gap_list)}')