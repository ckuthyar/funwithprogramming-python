s1="SindhuAnumolu"
len1=len(s1)
spacer=" "
for j in range(1,len1+1,1):
    for i in range(0,len1-j,1):
        print(spacer,end="")
    print(s1[0:j])
for j in range(1,len1,1):
    for i in range(0,j,1):
        print(spacer,end="")
    print(s1[0:len1-j])

