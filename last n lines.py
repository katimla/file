

f=open("last_line","r")
a=f.read().split()
i=-1
while i>-len(a):
    print(a[i])
    i=i-1
    break



