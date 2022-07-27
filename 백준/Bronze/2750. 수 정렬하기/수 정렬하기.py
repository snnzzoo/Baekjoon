T = int(input())
numbers = []

for t in range(T):
    numbers.append(int(input()))

numbers.sort()

for n in range(T):
    print(numbers[n])
    
    