def remov(num,val):
    k=0
    for i in num:
        if i!=val:
           num[k]=i
           k+=1
           
    return k
num=[2,3,4,5,6] 
val=3     
print(remov(num,val))  