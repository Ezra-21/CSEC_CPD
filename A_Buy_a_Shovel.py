cost,r = map(int,input().split())
temp = cost
num_shovel = 1
while True:
    if (cost%10==0) or (cost%10==r):
        break
    num_shovel+=1
    cost+=temp
    
    
print(num_shovel)