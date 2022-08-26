total_list = []

for i in range(5):
    score = map(int, input().split())
    # print(score)
    total = sum(score)
    # print(total)
    total_list.append(total)
print(total_list.index(max(total_list))+1, max(total_list))
