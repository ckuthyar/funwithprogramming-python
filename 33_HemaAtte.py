f1=open("paner_family_kan2.txt","r")
f2=open("paner_family3.txt","w")
info1=f1.readlines()
info2=[]
len1=len(info1)
for i in range(0,len1,1):
    info2.append(info1[i].replace("\n",""))
    f2.write(info2[i])
    f2.write(" ")
f2.close()
print(info2)
