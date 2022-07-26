T = int(input())
O = 'O'
X = 'X'

for t in range(T):
    ox = input()
    count_o = 0
    sum_ = 0

    for answer in ox:
        if answer == O:
            count_o += 1
            sum_ += count_o
        elif answer == X:
            count_o = 0
            
    print(sum_)