for j in range(0,12,1):
    for i in range(0,12,1):
        time1=(str(9+j)+":"+str(i*5))
        angle1=((90-j*30)+i*30-i*2.5)
        print(time1,"-",angle1%360)
    print()
