# a=["SBI","HDFC","RBL"]
# file=open("bank.txt","w")
# i=0
# while i<len(a):
#     file.write(""+a[i]+"\n")
#     i=i+1
# file.close()

# a=["SBI","HDFC"]
# f=open("mango.txt","r")
# d=f.read()
# i=0
# while i<len(a):
#     i=i+1
# print(d)
# f.close()


# a=["SBI","HDFC"]
f=open("mango.txt","r")
d=f.readlines()
i=-1
while i>=-len(d):
    print(d[i])
    i-=1
f.close()

