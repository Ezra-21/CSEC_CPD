l,b = map(int,input().split())
year = 0
while l<=b:
    l*=3
    b*=2
    year+=1
print(year)