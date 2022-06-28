f=open("end.txt","r")
a=f.read()
b=a.split()
i=0
while i<len(b):
    if "ing" in b[i]:
        b.remove(b[i])
    else:
        print(b[i],end=",")
    i=i+1


# f=open("end","r")
# a=f.read()
# print(a)
# x=a.split()
# i=0
# c=0
# while i<len(x):
#     if "ing" in x[i]:
#         c+=1
#     i+=1
# print("the count is",c)
# f.close()