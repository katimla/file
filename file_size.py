# f=open("file_size.txt","r")
# a=f.read()
# print("file size is:",f.tell(),"katimla")

def getSize(fileobject):
    fileobject.seek(0,2) # move the cursor to the end of the file
    size = fileobject.tell()
    return size

file = open('jai.txt', 'rb')
print (getSize(file)) 