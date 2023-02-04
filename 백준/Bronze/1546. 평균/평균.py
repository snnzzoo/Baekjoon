N = int(input())
score = list(map(int, input().split()))
new_score = []

for n in range(N):
    new_score.append(score[n] / max(score) * 100)

print(sum(new_score) / N)