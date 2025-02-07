num = int(input())
arr = list(map(int, input().split()))
left,right = 0,len(arr)-1
sereja,dima = 0,0
while left<=right:
    if arr[left]>=arr[right]:
        sereja+=arr[left]
        left+=1
    else:
        sereja+=arr[right]
        right-=1
    if left<=right:
        if arr[left]>=arr[right]:
            dima+=arr[left]
            left+=1
        else:
            dima+=arr[right]
            right-=1
print(sereja,dima)
