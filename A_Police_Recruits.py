n = int(input())
arr = list(map(int,input().split()))
crime = 0
police = 0
for event in arr:
    if event == -1:
        if police > 0:
            police-=1
        else:
            crime+=1
    else:
        police+=event
print(crime)