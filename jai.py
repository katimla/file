f=open("jai.txt","r")
a=[]

for i in f:
    b=i.strip()
    x=b.split("-")
    a.extend(x)
print(a)
f.close()
    
    