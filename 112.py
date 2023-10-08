def malware1():
    import os
    info=os.listdir()
    fname=(info[133])
    print(fname)
    list1=[]
    f1=open(fname,"r")
    for i in range(0,3,1):
        list1.append(f1.readline())
    print(list1)
    print(list1[132])
    return(list1)

result=malware1()
print(result)
