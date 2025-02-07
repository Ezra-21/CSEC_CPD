game = []
for _ in range(int(input())):
    arr = list(map(int,input().split()))
    game.append(arr)
    
count = 0

for i in range(len(game)):
    for j in range(len(game)):
        if game[i][0] == game[j][1]:
            count+=1
print(count)