word = input()
count_lower = 0
for char in word:
    if char > 'Z':
        count_lower+=1
if count_lower<(len(word)+1)//2:
    print(word.upper())
else:
    print(word.lower())

        