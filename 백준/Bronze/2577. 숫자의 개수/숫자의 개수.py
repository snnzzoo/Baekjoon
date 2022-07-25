a = int(input())
b = int(input())
c = int(input())
result = list(str((a * b * c)))
              
for number in range(0, 10):
    print(result.count(str(number)))