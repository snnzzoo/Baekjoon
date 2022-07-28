N = list(map(int, input().split()))

number_s = N[0] // 2
number_a = N[1] // 2

if number_s > number_a:
    print(number_a)
else:
    print(number_s)