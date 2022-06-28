file=open("vovel_consonant.txt","r")
a=file.read()
print(a)
vovel=0
consonant=0
i=0
while i<len(a):
    if a[i] in ("a","e","i","o","u","A","O","I"):
        vovel=vovel+1
    elif a[i] in ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","B","I"):
        consonant=consonant+1
    i=i+1
print(vovel)
print(consonant)
                