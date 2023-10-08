def atoz1():
    upper=[]
    lower=[]
    asc_upper=[]
    asc_lower=[]
    letter_upper="A"
    letter_lower="a"

    for i in range(0,26,1):
        ascii1=ord(letter_upper)+i
        letter1=chr(ascii1)
        
        ascii2=ord(letter_lower)+i
        letter2=chr(ascii2)
        
        upper.append(letter1)
        lower.append(letter2)
        asc_upper.append(ascii1)
        asc_lower.append(ascii2)
        
    print(upper)
    print(lower)

    print(asc_upper)
    print(asc_lower)

