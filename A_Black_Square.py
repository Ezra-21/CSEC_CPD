arr = list(map(int,input().split()))
idx = input()
ans = 0
for val in idx:
    ans+=arr[int(val)-1]
print(ans)