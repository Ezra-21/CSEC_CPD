mat = []
for _ in range(5):
    arr = list(map(int, input().split()))
    mat.append(arr)

for i in range(5):
    for j in range(5):
        if mat[i][j] == 1:
            print(abs(i - 2) + abs(j - 2))
            break