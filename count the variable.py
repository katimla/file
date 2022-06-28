


# f=open("katimla.txt","r")
# a=f.read()
# count=0
# i=0
# c=0
# c1=0
# c2=0
# c3=0
# c4=0
# while i<len(a):
#     if "s" in a[i]:
#         c=c+1
#     elif "c" in a[i]:
#         c1=c1+1
#     elif "h" in a[i]:
#         c2=c2+1
#     elif "o" in a[i]:
#         c3=c3+1
#     elif "l" in a[i]:
#         c4=c4+1
#     i=i+1
# print("s:",c)
# print("c:",c1)
# print("h:",c2)
# print("o:",c3)
# print("l:",c4)
# f.close()



# list="my name is katimla"
# l2=[]
# i=0
# while i<len(list):
#     if list[i] not in l2 and list[i]!=" ":
#         l2.append(list[i])
#     i+=1
# i=0
# d=[]
# while i<len(l2):
#     j=0
#     c=0
#     while j<len(list):
#         if l2[i]==list[j]:
#             c+=1
#         a=l2[i],c
#         j+=1 
#     d.append(a)
#     i+=1
# print(d)



i=1
while i<=5:
    j=1
    while j<=i:
        print("#",end=" ")
        j=j+1
    print()
    i=i+1