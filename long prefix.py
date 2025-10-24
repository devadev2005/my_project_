long=['flower','fit','fluke']
long=sorted(long)
f=long[0]
l=long[-1]

ans=''
for i in range(min(len(f),len(l))):
     if f[i]==l[i]:
          ans+=f[i]
     else:
         break
        
print(ans)     