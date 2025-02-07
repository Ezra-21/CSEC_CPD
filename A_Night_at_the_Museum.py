word = input()
ans = 0
previos = 0
for char in word:
    current = ord(char)-ord('a')
    ans += min(abs(current-previos),26-abs(current-previos))
    previos = current
print(ans)