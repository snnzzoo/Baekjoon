N = input().split()

rev_x = int(N[0][::-1])
rev_y = int(N[1][::-1])

rev_sum = rev_x + rev_y
print(int(str(rev_sum)[::-1]))
