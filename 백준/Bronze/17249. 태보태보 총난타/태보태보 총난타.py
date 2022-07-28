t = input()
t_split = t.split('(^0^)')

t_left = t_split[0]
t_right = t_split[1]

print(t_left.count('@'), t_right.count('@'))
    