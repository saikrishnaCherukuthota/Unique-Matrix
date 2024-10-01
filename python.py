
n=int(input())
l=list(range(1,1+n))
result1=True
list1=[]
for j in range(n):
    list2=list(map(int,input().split(" ")))
    if sorted(list2)!=l:
        result1=False
        break
print(result1)


