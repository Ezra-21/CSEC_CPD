y,w = map(int,input().split())
maxi = max(y,w)
hashh = {1:'1/1',2:'5/6',3:'2/3',4:'1/2',5:'1/3',6:'1/6'}
print(hashh[maxi])