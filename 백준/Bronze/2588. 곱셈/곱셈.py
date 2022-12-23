A = int(input())
B = int(input())

a = B // 100
b = B // 10 - ((B // 100) * 10)
c = B % 10

print(c * A)
print(b * A)
print(a * A)
print(A * B)