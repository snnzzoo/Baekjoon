while True:
    data = input()
    cnt = 0
    
    if data == '#': # 입력 끝, 반복문 종료
        break
    for _ in data:
        if _ in 'aeiouAEIOU':
            cnt += 1
    print(cnt)