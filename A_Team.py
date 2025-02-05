ans = 0
for _ in range(int(input())):
    arr = list(map(int, input().split()))
    if sum(arr)>1:
        ans+=1
print(ans)