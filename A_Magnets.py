n = 0
count = 0
for _ in range(int(input())):
    num = int(input())
    if num!=n:
        count+=1
    n = num
print(count)
    