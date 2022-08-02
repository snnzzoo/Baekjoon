N, M = input().split()
A = list(input().split())
B = list(input().split())

a_b = list(set(A) - set(B))
b_a = list(set(B) - set(A))

print(len(a_b) + len(b_a))