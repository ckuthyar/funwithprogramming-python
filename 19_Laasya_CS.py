num1=int(input("Enter the number"))
num2=int(input("Enter the number"))

for j in range(num1,num2+1):
    for i in range(1,11):
        product = str(j)+" "+str(i)+" "+str(i*j)
        print(product)
    print()
    
    
