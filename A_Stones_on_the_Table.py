num = int(input())
color = input()
ans = 0
i,j = 1,0
while i<num:
    if color[i]==color[j]:
        ans+=1
    else:
        j=i
    i+=1
print(ans)

    
    