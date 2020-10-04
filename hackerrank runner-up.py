x = int(input())
lis = [int(x) for x in input().split()]   
# i = int(input())
# lis = list(map(int,input().strip().split()))[:i]
z = max(lis)
while max(lis) == z:
    lis.remove(max(lis))

print (max(lis))