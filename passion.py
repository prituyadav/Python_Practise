arr=[1,2,3,4]
c1=c2=c3=c4=divisble=0
length=len(arr)
print("Array length:",length)
for x in range(0, 4):
    print(arr[x])
    if (arr[x]%5)==0:
        c1=c1+1 
        divisble=1 
    if(arr[x]%3)==0:
        c2=c2+1 
        divisble=1 
    if(arr[x]%2)==0:
        c3=c3+1 
        divisble=1 
    else: c4 = c4 + divisble
print(c1,c2,c3,c4)
