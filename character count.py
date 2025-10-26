n=input()
count={}

for i in n:
    if i in count:
        count[i]+=1
    else:
        count[i]=1
print(count)
printed=set()        
for char , frq in count.items():
    if i not in printed:
         print(f"{char}:{frq}")
         printed.add(frq)
        
    

