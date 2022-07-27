numbers = [int(input()) for n in range(9)]

print(max(numbers))
print(numbers.index(max(numbers)) + 1)