def findTopper(file1):
    
    names = []
    subjects = []
    sub1 = []
    sub2 = []
    sub3 = []
    sub4 = []
    sub5 = []
    topper_sub1 = []
    topper_sub2 = []
    topper_sub3 = []
    topper_sub4 = []
    topper_sub5 = []

    f1 = open(file1, "r")
    list1 = f1.readlines()
    len1 = len(list1)

    for i in range(len1):
        list2 = list1[i].split(",")
        
        names.append(list2[0])
        
        list3 = list2[3].split(":")
        subjects.append(list3[0])
        sub1.append(int(list3[1]))
        
        list3 = list2[4].split(":")
        subjects.append(list3[0])
        sub2.append(int(list3[1]))

        list3 = list2[5].split(":")
        subjects.append(list3[0])
        sub3.append(int(list3[1]))

        list3 = list2[6].split(":")
        subjects.append(list3[0])
        sub4.append(int(list3[1]))

        list3 = list2[7].split(":")
        subjects.append(list3[0])
        sub5.append(int(list3[1]))

    maxsub1 = max(sub1)
    maxsub2 = max(sub2)
    maxsub3 = max(sub3)
    maxsub4 = max(sub4)
    maxsub5 = max(sub5)

    for i in range(len1):
        if sub1[i] == maxsub1:
            topper_sub1.append(names[i])
        if sub2[i] == maxsub2:
            topper_sub2.append(names[i])
        if sub3[i] == maxsub3:
            topper_sub3.append(names[i])
        if sub4[i] == maxsub4:
            topper_sub4.append(names[i])
        if sub5[i] == maxsub5:
            topper_sub5.append(names[i])

    print(topper_sub1, "are the toppers in ",subjects[0]," with marks", maxsub1)
    print(topper_sub2, "are the toppers in ",subjects[1]," with marks", maxsub2)
    print(topper_sub3, "are the toppers in ",subjects[2],"with marks", maxsub3)
    print(topper_sub4, "are the toppers in ",subjects[3]," with marks", maxsub4)
    print(topper_sub5, "are the toppers in ",subjects[4]," with marks", maxsub5)

