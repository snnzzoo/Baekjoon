numbers = [int(input()) for i in range(10)]
result = []

for j in range(len(numbers)):
    result.append(numbers[j] % 42)
    
print(len(list(set(result))))
