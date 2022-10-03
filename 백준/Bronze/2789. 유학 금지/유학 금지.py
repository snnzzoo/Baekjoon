cambridge = ['C', 'A', 'M', 'B', 'R', 'I', 'D', 'G', 'E']
word = input()
result = ''

for i in word:
    if i not in cambridge:
        result += i
        
print(result)