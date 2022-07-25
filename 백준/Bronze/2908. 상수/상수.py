a, b = map(int, input().split())
result_a = int(str(a)[::-1])
result_b = int(str(b)[::-1])
result_list = [result_a, result_b]
max_number = result_list[0]

for number in range(2):
    if result_list[number] > max_number:
        max_number = result_list[number]
print(max_number)