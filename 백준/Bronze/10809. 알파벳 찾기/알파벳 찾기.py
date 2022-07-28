word = input()
alphabet = [chr(i) for i in range(97, 123)]

for a in alphabet:
    print(word.find(a), end=' ')