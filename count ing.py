f=open("or.txt","r")
a=f.read()
print(a)
x=a.split()
i=0
c=0
while i<len(x):
    if "ing" in x[i]:
        c+=1
    i+=1
print("the count is",c)
f.close()

# f=open("or.txt","a")
# f.writlines("count the variable")
# f.close()