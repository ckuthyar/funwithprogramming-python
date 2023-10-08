def show():
    for j in range(0,10,1):
        for i in range(0,10,1):
            print(crossword[i+j*10],end="")
        print()
    print()


words=['EAT','APPLE','MEN','AM','LION','SUIT','TO','TRAIN','CAP','ME','LEMON','MASTER','RINSE','IT', 'NEST']
lastchar=""
eligible=[]
len_eligible=[]
maxlen_eligible=0
chosen=''
len_chosen=0
lenw=len(words)
print(lenw)
crossword=[]
for i in range(0,100,1):
    crossword.append("$")
show()




chosen=words[0]
list1=list(chosen)
len1=len(list1)

for i in range(0,len1,1):
    crossword[i]=words[0][i]
    lastchar=crossword[i]
show()
words.remove(chosen)
lenw=len(words)
print(words)


for i in range(0,lenw,1):
    if(words[i][0]==lastchar):
        eligible.append(words[i])
        len_eligible.append(len(words[i]))
maxlen_eligible=max(len_eligible)
for i in range(0,len(eligible),1):
    if(maxlen_eligible==len_eligible[i]):
        chosen=eligible[i]
list1=list(chosen)
len1=len(list1)

print(chosen)
print(len1)
for i in range(1,len1,1):
    crossword[2+i*10]=chosen[i]
lastchar=chosen[i]

show()
words.remove(chosen)
lenw=len(words)
print(words)


eligible=[]
len_eligible=[]
for i in range(0,lenw,1):
    if(words[i][0]==lastchar):
        eligible.append(words[i])
        len_eligible.append(len(words[i]))
maxlen_eligible=max(len_eligible)
for i in range(0,len(eligible),1):
    if(maxlen_eligible==len_eligible[i]):
        chosen=eligible[i]
len_chosen=len(chosen)
print(chosen)
print(len_chosen)

for i in range(0,4,1):
    crossword[4*10+3+i-1]=chosen[i]
lastchar=chosen[i]

show()
eligible=[]
len_eligible=[]
for i in range(0,lenw,1):
    if(words[i][0]==lastchar):
        eligible.append(words[i])
        len_eligible.append(len(words[i]))
maxlen_eligible=max(len_eligible)
for i in range(0,len(eligible),1):
    if(maxlen_eligible==len_eligible[i]):
        chosen=eligible[i]
len_chosen=len(chosen)
print(chosen)
print(len_chosen)

for i in range(0,1,1):
    crossword[5*10+5+i]=chosen[i+1]
    print(chosen[i+1])
lastchar=chosen[i]

crossword[55]="0"
show()
lastchar="T"
eligible=[]
len_eligible=[]
for i in range(0,lenw,1):
    if(words[i][0]==lastchar):
        eligible.append(words[i])
        len_eligible.append(len(words[i]))
maxlen_eligible=max(len_eligible)
for i in range(0,len(eligible),1):
    if(maxlen_eligible==len_eligible[i]):
        chosen=eligible[i]
len_chosen=len(chosen)
print(chosen)
print(len_chosen)
