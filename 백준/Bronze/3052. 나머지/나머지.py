numbers = [int(input()) for n in range(10)]
remainders = []

for n in numbers:
    remainders.append(n % 42)
    
remainders_set = set(remainders)
print(len(remainders_set))

