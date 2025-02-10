strr = input()
instruct = input()

position = 1
j = 0
for step in instruct:
    if step == strr[j]:
        position += 1
        j+=1
print(position)
