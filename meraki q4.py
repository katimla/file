# file=open("question.txt","x")
# file.create()

delhi=open("del.txt","w")
meerut=open("mee.txt","w")
shimla=open("shim.txt","w")
cochin=open("coc.txt","w")
jaipur=open("jai.txt","w")
tokyo=open("tok.txt","w")
kanpur=open("kan.txt","w")
raipur=open("rai.txt","w")
f=open("question.txt","r")
a=f.read()
b=a.split("\n")
i=0
while i<len(b):
    if "delhi" in b[i]:
        delhi.write(b[i])
        delhi.write("\n")
    elif "meerut" in b[i]:
        meerut.write(b[i])
        meerut.write("\n")
    elif "shimla" in b[i]:
        shimla.write(b[i])
        shimla.write("\n")
    elif "cochin" in b[i]:
        cochin.write(b[i])
        cochin.write("\n")
    elif "jaipur" in b[i]:
        jaipur.write(b[i])
        jaipur.write("\n")
    elif "tokyo" in b[i]:
        tokyo.write(b[i])
        tokyo.write("\n")
    elif "kanpur" in b[i]:
        kanpur.write(b[i])
        kanpur.write("\n")
    else:
        raipur.write(b[i])
        raipur.write("\n")
    i+=1
f.close()