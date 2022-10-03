word = input()
cambridge = 'CAMBRIDGE'

for i in word:
    if i in cambridge:
        word = word.replace(i, '')

print(word)